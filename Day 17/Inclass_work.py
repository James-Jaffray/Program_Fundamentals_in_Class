
student = {
"name": "Alex",
"age": 21,
"major": "Physics",
"grades": [88, 92, 79]
}


for key in student: # Loop through keys
    # Access value using key
    print(f"{key}: {student[key]}")


name = student.get("name", "N/A")
print("First name:", name)
