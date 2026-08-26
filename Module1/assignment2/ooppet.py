class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def descibe(self):
        return (f'{self.name} is a {self.age}-year-old-{self.species}')


pet1 = Pet('Rex','Dog',3)
pet2 = Pet('Luna','Cat',2)
pet3 = Pet('Kiwi' 'Parrot',1)

