a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


def greatest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(f"The greatest number is: {greatest_number(a, b, c)}")