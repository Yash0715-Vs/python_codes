name = input("Enter your name: ")

mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))   
mark3 = int(input("Enter marks for subject 3: "))
mark4 = int(input("Enter marks for subject 4: "))

total_marks = mark1 + mark2 + mark3 + mark4
total_percentage = (total_marks / 400) * 100

if total_percentage >= 60:
    print("you have passed the exam.")
else:
    print("you have failed the exam.")

print(f"Total marks obtained: {total_marks}")
print(f"Total percentage: {total_percentage:.2f}%")
print(f"Thank you, {name}!")
