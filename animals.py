from typing import List

class Animal:
    def __init__(self, id: int, species: str, name: str, age: int, gender: str, colour: str, weight: float):
        self.id = id
        self.species = species
        self.name = name
        self.age = age
        self.gender = gender
        self.colour = colour
        self.weight = weight


    def __str__(self):
        return f'id {self.id}. {self.species}: {self.name} {self.age} years old, {self.gender} {self.colour}, {self.weight}'
    

    def __repr__(self):
        return f"Animal(id={self.id!r}, species={self.species!r}, name={self.name!r}, age={self.age!r}, gender={self.gender!r}, colour={self.colour!r}, weight={self.weight!r})"
        

def menu_printing() -> None:
    print("1: Dodaj nowe zwierzę")
    print("2: Wyświetl wszystkie zwierzęta")
    print("3: Zmodyfikuj dane wybranego zwierzęcia")
    print("4: Usuń zwierzę z biblioteki")
    print("5: Zakończ program")


def find_next_id(animals: List[Animal]):
    counter = 1
    ids = [animal.id for animal in animals]
    while counter in ids:
        counter += 1
    return counter


def creating_animal(animals: List[Animal]) -> Animal:
    species = input("Podaj gatunek zwierzęcia: ").lower().strip()
    name = input("Podaj imię zwierzęcia: ").capitalize().strip()
    age = int(input("Podaj wiek zwierzęcia w latach: "))
    gender = input("Podaj płeć zwierzęcia: ").lower().strip()
    colour = input("Podaj kolor zwierzęcia: ").lower().strip()
    weight = float(input("Podaj wagę zwierzęcia w kilogramach: "))
    id = find_next_id(animals)
    return Animal(id, species, name, age, gender, colour, weight)




def main():
    animals = []
    while True:
        menu_printing()
        try:
            choice = int(input('Co chcesz zrobić, wpisz odpowiednią cyfrę: '))
        except:
            print("Błąd! Wpisz liczbę od 1 do 5")
            continue

        if choice == 1:
            new_animal = creating_animal(animals)
            animals.append(new_animal)
            print("Dodano poniższe zwierzę:\n", new_animal)
            print(animals)

        else:
            break
        




if __name__ == '__main__':
    main()
