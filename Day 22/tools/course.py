class Course:
    def __init__(self, name: str) -> None:
        self.name = name
        self.students = []
        self.assignments = []

    def __str__(self) -> str:
        return f"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments"



