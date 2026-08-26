# Made a Pet class that has name, species, and age as parameters
class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    # Made the describe method that returns an f string containing the name, age, and species.
    def describe(self):
        return (f'{self.name} is a {self.age}-year-old-{self.species}\n')
     
    
# Made the pets list and defined main
def main():
    pets = [
        Pet('Rex','Dog', 3),
        Pet('Luna','Cat', 2),
        Pet('Kiwi', 'Parrot', 1)
    ]

    # Made a for loop that iterates over pets, then calls the describe method to print the information
    for p in pets:
        print(p.describe())
main()