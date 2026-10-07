student_age = []
student_age_sum = 0
student_age_avg = 0
counter = 0


print('Average age of students calculator')

while True:
    user_input = input("Enter the age of a student or 'stop' to finish: ").lower()
    if user_input == 'stop':
            break
    else:
        user_input = int(user_input)
        student_age.append(user_input)
        student_age_sum = student_age_sum + user_input
        counter = counter + 1


student_age_avg = student_age_sum / counter
print(f'The average age of the students is {student_age_avg}')