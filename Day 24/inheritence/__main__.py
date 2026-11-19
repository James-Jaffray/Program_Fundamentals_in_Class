from animals import Dog, Cat, Bird


def main() -> None:
    # create the animals
    dog = Dog("Ranger", "Brown", 4, "Labrador")
    cat1 = Cat("Cat 1", "Black", 4, "tuxedo", 5)
    cat2 = Cat("Cat 2", "Orange", 4, "Tabby", 15)
    cat3 = Cat("Cat 3", "White", 4, "Solid Color", 25)
    bird = Bird("Furry Birdy", "Green", 2, 5.45)
    
    # add animals to list
    animals = [dog, cat1, cat2, cat3, bird]

    # loop through the attributes and methods of each animal
    for animal in animals:
        print("-----------------")
        print(animal)
        
        animal.make_a_noise()
        animal.move()
        animal.eat()
        # check that the animal is a dog before executing chase_car()
        if isinstance(animal, Dog):
            animal.chase_car()
        
        print("-----------------")

if __name__ == "__main__":
    main()
