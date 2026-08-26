class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def describe(self):
        return (f'{self.name} is a {self.age}-year-old-{self.species}')

pets = [
    Pet('Rex','Dog', 3),
    Pet('Luna','Cat', 2),
    Pet('Kiwi', 'Parrot', 1)
]

for p in pets:
    print(p.describe())