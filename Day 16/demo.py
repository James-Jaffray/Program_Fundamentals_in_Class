def show_info(name, age):
    print(f"{name} is {age} years old.")

person = ("Alice", 30)
show_info(*person)

settings = {"name": "Bob", "age": 25}
show_info(**settings)

