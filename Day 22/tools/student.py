class Student:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.submissions = []

    def __str__(self) -> str:
        return f"{self.name}"
