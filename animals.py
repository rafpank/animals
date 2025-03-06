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
        return f'id {self.id}. Zwierze to {self.gender} gatunku: {self.species} ma na imię {self.name} skończył(a) już {self.age} lat, ma kolor {self.colour}  i waży {self.weight} kg'
    

    def __repr__(self):
        return f"Animal(id={self.id!r}, species={self.species!r}, name={self.name!r}, age={self.age!r}, gender={self.gender!r}, colour={self.colour!r}, weight={self.weight!r})"
        

def menu_printing() -> None:
    print("\n1: Dodaj nowe zwierzę")
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

def finding_animal(animals: List[Animal], user_id_choice: int) -> Animal | None:
    for animal in animals:
        if animal.id == user_id_choice:
            return animal
    return None

def animal_modification(animals: List[Animal], user_id_choice: int) -> str:
    # found = False
    animal = finding_animal(animals, user_id_choice)

    if animal is None:
        return "Nie znaleziono zwierzęcia o podanym ID"  
  
    print(f"Wybrane zwierzę to: \n{animal}")

    print("\nKtóre dane chcesz zmienić?")
    print("1: Gatunek\n2: Imię\n3: Wiek\n4: Płeć\n5: Kolor\n6: Waga\n7: Anuluj wybór")
    field_choice = int(input("Wpisz numer pola: "))

    new_value = input("Podaj nową wartość: ").strip()

    if field_choice == 1:
        animal.species = new_value.lower()
    elif field_choice == 2:
        animal.name = new_value.capitalize()
    elif field_choice == 3:
        animal.age = int(new_value)
    elif field_choice == 4:
        animal.gender = new_value.lower()
    elif field_choice == 5:
        animal.colour = new_value.lower()
    elif field_choice == 6:
        animal.weight = float(new_value)
    elif field_choice == 7:
        return "Anulowano wybór"
    else:
        print("Niepoprawny wybór")

    found = True
    return f"Zakutalizowano dane zwierzęcia:\n {animal}"
          

def deleting_animal(animals: List[Animal], user_id_choice: int) -> str:
    animal = finding_animal(animals, user_id_choice)

    if animal is None:
        return "Nie znaleziono zwierzęcia o podanym ID"
   
    user_aproval = input(f"Czy potwierdzasz chęć usunięcia {animal} z bazy? [t/n]: ").lower()
    if user_aproval == 't':
        animals.remove(animal)
        return f"Pozstała lista zwierząt: {animals}"
    else:
        print("Anulowano wybór")
    

    return animals


def main():
    animals = [
        Animal(id=1, species='kot', name='Pączka', age=11, gender='samiczka', colour='szary', weight=4.0),
        Animal(id=2, species='pies', name='Teddy', age=2, gender='samiec', colour='biało-brązowy', weight=5.0)
    ]
    
    while True:
        menu_printing()
        try:
            choice = int(input('Co chcesz zrobić, wpisz odpowiednią cyfrę:\n'))
        except ValueError:
            print("Błąd! Wpisz liczbę od 1 do 5")
            continue

        if choice == 1:
            new_animal = creating_animal(animals)
            animals.append(new_animal)
            print(f"Dodano poniższe zwierzę:\n {new_animal}\n")
        
        elif choice == 2:
            if animals:
                print("Lista zwierząt:")
                for animal in animals:
                    print(animal)
            else:
                print("Brak zwierząt w bazie")
        
        elif choice == 3:
            user_id = int(input('Podaj ID zwierzęcia, którego dane chcesz zmodyfikować: '))
            print(animal_modification(animals, user_id))

        elif choice == 4:
            user_id = int(input("Które zwierzę chcesz usunąć? Podaj nr ID: "))
            print(deleting_animal(animals, user_id))

        elif choice == 5:
            break

        else:
            print("Nieprawidłowy wybór")
        




if __name__ == '__main__':
    main()
