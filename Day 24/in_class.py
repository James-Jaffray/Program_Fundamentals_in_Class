class Animal:
    def __init__(self, name: str, color: str, num_legs: int):
        self.name = name
        self.color = color
        self.num_legs = num_legs

    def eat(self) -> None:
        print(f"{self.name} starts eating. Nom nom nom .")

    def make_a_noise(self) -> None:
        print(f"{self.name} makes an interesting noise.")

    def move(self) -> None:
        print(f"{self.name} runs around!")
        
    def __str__(self) -> str:
        return f"Name: {self.name}\nColor: {self.color}"