a = int(input("Enter your age: "))
if a >=18:
    print("You are eligible to vote.")
    print("You can also apply for a driving license.")

elif a < 0:
    print("Invalid input. Please enter a valid age.")

elif a == 0:
    print("You are not eligible to vote.")
    print("You cannot apply for a driving license.")
else:
    print("You are not eligible to vote.")
    print("You cannot apply for a driving license.")

print("Thank you.")