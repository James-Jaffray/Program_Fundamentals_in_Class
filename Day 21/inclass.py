def shout(name: str) -> None:
    print(f"HEY {name.upper()}!")

class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year



my_car = Car("Toyota", "Corolla", 2020)
print(my_car.make) # Output: Toyota
print(my_car.model) # Output: Corolla

second_car = Car("Honda", "Civic", 2021)
print(second_car.year) # Output: 2021
print(second_car.make) # Output: Honda


class Car:
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model
    def honk(self) -> None:
        print(f"{self.make} {self.model} says beep beep!")

my_car = Car("Honda", "Civic")
my_car.honk()
# note you didn't have to pass `self` here, it is passed automatically


class Car:
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model
    def __str__(self) -> str:
        return f"{self.make} {self.model}"
    
my_car = Car("Ford", "Focus")
print(my_car) # Output: Ford Focus


class Car:
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model
    def __repr__(self) -> str:
        return f"Car(make='{self.make}', model='{self.model}')"

my_car = Car("Subaru", "Impreza")
print(repr(my_car)) # Output: Car(make='Subaru', model='Impreza')



class Garage:
    def __init__(self) -> None:
        self.cars = []

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def list_cars(self) -> None:
        for car in self.cars:
            print(car)

            
garage = Garage()
garage.add_car(Car("Mazda", "3"))
garage.add_car(Car("Tesla", "Model 3"))
garage.list_cars()