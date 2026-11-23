class Dog:
    def __init__(self, name):
        self.name = name

    def sit(self):
        return F"{self.name} sit"

obj = Dog("gary")
obj.name = "steve"
print(obj.sit())