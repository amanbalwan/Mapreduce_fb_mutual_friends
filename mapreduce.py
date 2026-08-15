from collections import defaultdict
class Mapreduce:
    def __init__(self):
        self.friend_list={
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

        self.pair_count=defaultdict(int)

        for key,values in self.friend_list.items():
            values.sort()
            for i in range(len(values)):
                for j in range(i+1,len(values)):
                    self.pair_count[(values[i],values[j])]+=1

    def map_reduce(self,friends):
        friends.sort()
        print(self.pair_count[(friends[0],friends[1])])

m = Mapreduce()

while True:
    person = input("Enter two friends: ")
    if person.lower() == "exit":
        print("Goodbye!")
        break
    names = person.split()
    m.map_reduce(names)