class Animal:
    def __init__(self, species, name, age, gender, color, weight):
        self.species = species
        self.name = name
        self.age = age
        self.gender = gender
        self.color = color
        self.weight = weight


    def __str__(self):
        return f'{self.species}: {self.name} {self.age} years old, {self.gender} {self.color}, {self.weight}'
        