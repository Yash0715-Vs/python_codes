def inch_to_cm(inches):
    return inches * 2.54

inches = float(input("Enter length in inches: "))
print(f"{inches} inches is equal to {inch_to_cm(inches)} centimeters.")