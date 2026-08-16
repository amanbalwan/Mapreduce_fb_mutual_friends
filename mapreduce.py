from collections import defaultdict
from multiprocessing import Pool, cpu_count
from time import perf_counter
import csv

class Mapreduce:
    def __init__(self,workers = None):
        self.friend_list = friend_list
        self.mutual_friends = self.run_map_reduce(self.friend_list, workers)

    def chunk_dict(self,data, n_chunks):
        items = list(data.items())
        if not items:
            return []
        chunk_size = max(1, len(items)//n_chunks + (1 if len(items)%n_chunks else 0) )
        return [dict(items[i:i+chunk_size]) for i in range(0,len(items),chunk_size)]
        
    def _map(self,friend_list):
        intermediate = []
        for person,friends in friend_list.items():
                friends.sort()
                person = person.lower()
                for i in range(len(friends)):
                    for j in range(i+1,len(friends)):
                        key = (friends[i].lower(),friends[j].lower())
                        intermediate.append((key,person))
        return intermediate

    def _shuffle(self,mapped_result):
        grouped = defaultdict(list)
        for chunk_result in mapped_result:
            for key, person in chunk_result:
                grouped[key].append(person)
        return grouped

    def _reduce_task(self,items):
        results = []
        for key,persons in items.items():
            results.append((key, sorted(set(persons))))
        return results

    def _flattern(self,results):
        ans=dict()
        for chunk in results:
            for key, value in chunk:
                ans[key]=value

        return ans

    def run_map_reduce(self, data, n_workers=None):
        n_workers = n_workers or min(cpu_count(),4)

        input_chunks = self.chunk_dict(data,n_workers)


        #map
        with Pool(n_workers) as pool:
            mapped_result = pool.map(self._map,input_chunks)

        #shuffle
        grouped = self._shuffle(mapped_result)

        #reduce
        input_chunks = self.chunk_dict(grouped,n_workers)

        with Pool(n_workers) as pool:
            reduced_result = pool.map(self._reduce_task,input_chunks)

        #flattern
        final = self._flattern(reduced_result)

        return final


    def get_mutual_friends(self, name1, name2):
        name1 = name1.strip().capitalize()
        name2 = name2.strip().capitalize()
        if name1 not in self.friend_list:
            return f"'{name1}' not found in friend list."
        if name2 not in self.friend_list:
            return f"'{name2}' not found in friend list."
        if name1 == name2:
            return "Please enter two different names."
    
        a,b = sorted([name1.lower(), name2.lower()])

        mutuals = self.mutual_friends.get((a,b),[])
        return mutuals
        
def load_friend_list ():
    friend_list = defaultdict(list)

    with open("facebook_friends_sample.csv", mode = "r", newline="", encoding= "utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != ["person","friend"]:
            raise ValueError(
            "CSV must have exactly these headers: person,friend"
        )

        for row in reader:
            person = row["person"].strip()
            friend = row["friend"].strip()

            if not person or not friend:
                continue

            friend_list[person].append(friend)

    return dict(friend_list)

if __name__ == "__main__":
    friend_list = load_friend_list()

    start_time = perf_counter()

    m = Mapreduce(1)

    end_time = perf_counter()

    print(f"MapReduce build time(Single-core): {end_time - start_time:.6f} seconds")

    start_time = perf_counter()
    
    m_multi = Mapreduce()

    end_time = perf_counter()

    print(f"MapReduce build time (Multi-processing): {end_time - start_time:.6f} seconds")
    


    while True:
        person = input("Enter two friends: ")
        if person.lower() == "exit":
            print("Goodbye!")
            break

        names = person.split()
        if len(names)!=2:
            print("Please enter just two names")
            continue

        result = m.get_mutual_friends(names[0],names[1])

        if isinstance(result,str):
            print(result)
        elif not result:
            print("No mutual friends. ")
        else:
            print(f"Mutual friends: ({len(result)}) : {','.join(result)} " )