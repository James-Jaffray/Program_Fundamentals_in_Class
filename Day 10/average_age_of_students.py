student_age = []
student_age_sum = 0



print('Average age of students calculator')

for i in student_age:
    age = input("Enter the age of a student or 'stop' to finish: ")

    if age.lower == 'stop':
        break
    else:
        age = int(age)
        if age > 0 and age < 100:
            student_age.append(age)
            print(student_age)
