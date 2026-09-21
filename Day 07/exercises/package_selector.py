pk_a_price = 40
pk_a_duration = 4

pk_b_price = 55
pk_b_duration = 8

pk_c_price = 75
pk_c_duration = 12

pk_d_price = 100
pk_d_duration = 12

print("Welcome to the Ultimate Gym")
print("Please select a membership package:")
print(f"- Package A: ${pk_a_price}/month, {pk_a_duration} months (short-term package)")
print(f"- Package B: ${pk_b_price}/month, {pk_b_duration} months (standard package)")
print(f"- Package C: ${pk_c_price}/month, {pk_c_duration} months (regular package)")
print(f"- Package D: ${pk_d_price}/month, {pk_d_duration} month (premium package, includes 4 free personal training sessions)")

selection = input("Enter the package letter (A/B/C/D): ").upper()

match selection:
    case "A":
        print(f"You have selected package {selection}")
        print(f"Your monthly fee is ${pk_a_price}")
        print(f"Your total fee is ${pk_a_price * pk_a_duration}")
    case "B":
        print(f"You have selected package {selection}")
        print(f"Your monthly fee is ${pk_b_price}")
        print(f"Your total fee is ${pk_b_price * pk_b_duration}")
    case "C":
        print(f"You have selected package {selection}")
        print(f"Your monthly fee is ${pk_c_price}")
        print(f"Your total fee is ${pk_c_price * pk_c_duration}")
    case "D":
        print(f"You have selected package {selection}")
        print(f"Your monthly fee is ${pk_d_price}")
        print(f"Your total fee is ${pk_d_price * pk_d_duration}")

    case _:
        print("Invalid selection. Please try again")