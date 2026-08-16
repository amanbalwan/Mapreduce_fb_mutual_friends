from collections import defaultdict
class Mapreduce:
    def __init__(self):
        self.friend_list=friend_list

        self.mutual_friends=self._map_reduce()
        
    def _map(self):
        intermediate = []
        for person,friends in self.friend_list.items():
                friends.sort()
                person = person.lower()
                for i in range(len(friends)):
                    for j in range(i+1,len(friends)):
                        key = (friends[i].lower(),friends[j].lower())
                        intermediate.append((key,person))
        return intermediate

    def _reduce(self,intermediate):
        grouped = defaultdict(list)
        for key, person in intermediate:
            grouped[key].append(person)
        return grouped


    def _map_reduce(self):
        intermediate = self._map()
        grouped = self._reduce(intermediate)
        return grouped

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
        
         

friend_list={
    "Alice": [
        "Ben",
        "Carol",
        "Cleo",
        "Ivan",
        "Karl",
        "Nina",
        "Uma"
    ],
    "Bob": [
        "Oscar",
        "Rita",
        "Tara"
    ],
    "Carol": [
        "Alice",
        "Nina"
    ],
    "Dave": [
        "Amy",
        "Ivan",
        "Judy",
        "Karl",
        "Oscar",
        "Uma"
    ],
    "Eve": [
        "Amy",
        "Drew",
        "Tara",
        "Victor"
    ],
    "Frank": [
        "Heidi"
    ],
    "Grace": [
        "Ivan",
        "Nina",
        "Yara"
    ],
    "Heidi": [
        "Frank",
        "Judy",
        "Xander"
    ],
    "Ivan": [
        "Alice",
        "Dave",
        "Drew",
        "Grace",
        "Mia"
    ],
    "Judy": [
        "Dave",
        "Heidi",
        "Paul",
        "Uma"
    ],
    "Karl": [
        "Alice",
        "Dave",
        "Sam",
        "Wendy"
    ],
    "Liam": [
        "Rita",
        "Xander",
        "Yara"
    ],
    "Mia": [
        "Cleo",
        "Drew",
        "Ivan",
        "Sam",
        "Victor"
    ],
    "Nina": [
        "Alice",
        "Carol",
        "Cleo",
        "Grace"
    ],
    "Oscar": [
        "Bob",
        "Dave",
        "Yara"
    ],
    "Paul": [
        "Cleo",
        "Judy",
        "Tara"
    ],
    "Quinn": [
        "Amy"
    ],
    "Rita": [
        "Bob",
        "Drew",
        "Liam",
        "Tara"
    ],
    "Sam": [
        "Karl",
        "Mia",
        "Zane"
    ],
    "Tara": [
        "Bob",
        "Eve",
        "Paul",
        "Rita"
    ],
    "Uma": [
        "Alice",
        "Dave",
        "Judy",
        "Zane"
    ],
    "Victor": [
        "Drew",
        "Eve",
        "Mia"
    ],
    "Wendy": [
        "Karl"
    ],
    "Xander": [
        "Drew",
        "Heidi",
        "Liam",
        "Zane"
    ],
    "Yara": [
        "Grace",
        "Liam",
        "Oscar"
    ],
    "Zane": [
        "Cleo",
        "Sam",
        "Uma",
        "Xander"
    ],
    "Amy": [
        "Cleo",
        "Dave",
        "Eve",
        "Quinn"
    ],
    "Ben": [
        "Alice"
    ],
    "Cleo": [
        "Alice",
        "Amy",
        "Mia",
        "Nina",
        "Paul",
        "Zane"
    ],
    "Drew": [
        "Eve",
        "Ivan",
        "Mia",
        "Rita",
        "Victor",
        "Xander"
    ]
    }

if __name__ == "__main__":

    m = Mapreduce()

    while True:
        person = input("Enter two friends: ")
        if person.lower() == "exit":
            print("Goodbye!")
            break

        names = person.split()
        if len(names)!=2:
            print("Please enter just two names")

        result = m.get_mutual_friends(names[0],names[1])

        if isinstance(result,str):
            print(result)
        elif not result:
            print("No mutual friends. ")
        else:
            print(f"Mutual friends: ({len(result)}) : {','.join(result)} " )