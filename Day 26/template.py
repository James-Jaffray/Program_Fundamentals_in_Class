class ClassName:                                   # CapWords, no parentheses unless inheriting

    # class attribute (optional): shared by every object
    shared_value = 0

    # constructor (dunder method); self is always first
    def __init__(self, parameter1: str, parameter2: int, parameter3: float = 0.0) -> None:
        # attributes: self.attribute_name = parameter
        self.attribute1 = parameter1
        self.attribute2 = parameter2
        self.attribute3 = parameter3               # parameter3 has a default value
        self.attribute4 = []                       # attribute not from a parameter

    # method: self first, then any other parameters
    def method_name(self, parameter: int) -> str:
        return f"{self.attribute1} {parameter}"    # use attributes via self.

    # dunder method: used by print(obj) and str(obj)
    def __str__(self) -> str:
        return f"ClassName({self.attribute1})"

    # dunder method: developer view
    def __repr__(self) -> str:
        return f"ClassName(attribute1: {self.attribute1})"


# inheritance: subclass of ClassName
class SubClassName(ClassName):
    def __init__(self, parameter1: str, parameter2: int, extra: str) -> None:
        super().__init__(parameter1, parameter2)   # run the parent's constructor
        self.extra = extra                         # the subclass's own attribute


# using it
obj = ClassName("a", 5)             # instantiate -> runs __init__
print(obj.attribute1)               # read an attribute
print(obj.method_name(3))           # call a method (self passed automatically)
print(obj)                          # calls __str__