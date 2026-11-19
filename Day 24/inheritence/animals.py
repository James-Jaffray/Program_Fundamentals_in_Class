class Animal:
    def __init__(self, name: str, color: str, num_legs: int) -> None:
        self.name = name
        self.color = color
        self.num_legs = num_legs

    def __str__(self) -> str:
        return f"Name: {self.name}\nColor: {self.color}\nNumber of Legs: {self.num_legs}"

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, color={self.color}, num_legs={self.num_legs})"

    def eat(self) -> None:
        print(f"{self.name} starts eating. Nom nom nom...")

    def make_a_noise(self) -> None:
        print(f"{self.name} makes an interesting noise.")

    def move(self) -> None:
        print(f"{self.name} runs around!")


class Dog(Animal):
    def __init__(self, name: str, color: str, num_legs: int, breed: str) -> None:
        super().__init__(name, color, num_legs)
        self.breed = breed

    def __str__(self) -> str:
    # call the Animal __str__() to get the name, color, and num_legs string.
        return_string = super().__str__() 
    # append the breed attribute of the dog
        return_string += f"\nBreed: {self.breed}"
    # return the updated string
        return return_string

    def make_a_noise(self) -> None:
        print(f"{self.name} starts barking loudly! Bark Bark!")

    def chase_car(self) -> None:
        print(f"{self.name} chases after a Honda Civic!")



class Cat(Animal):
    def __init__(self, name: str, color: str, num_legs: int, pattern: str, anger_level: int) -> None:
        super().__init__(name, color, num_legs)
        self.pattern = pattern
        self.anger_level = anger_level

    def __str__(self) -> str:
        return_string = super().__str__() 
        return_string += f"\nPattern: {self.pattern}"
        return_string += f"\nAnger level: {self.anger_level}"
        return return_string

    def make_a_noise(self) -> None:
        if  self.anger_level < 10:
            print(f"{self.name} Purr purr")
        elif  self.anger_level < 20:
            print(f"{self.name} Meow meow")
        else:
            print(f"{self.name} Hiss!")

    def knock(self) -> None:
        print(f"{self.name} Knocks things off a ledge")


class Bird(Animal):
    def __init__(self, name: str, color: str, num_legs: int, wingspan: float) -> None:
        super().__init__(name, color, num_legs)
        self.wingspan = wingspan

    def __str__(self) -> str:
        return_string = super().__str__() 
        return_string += f"\nWingspan: {self.wingspan}"
        return return_string

    def eat(self) -> None:
        print(f"{self.name} starts eating. Peck Peck Peck...")
    
    def move(self) -> None:
            print(f"{self.name} fly around!")

    def make_a_noise(self) -> None:
            print(f"{self.name} I want crackers")