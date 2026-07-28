# arithmetic operators
a= 10
b= 5
c= a + b  # addition
print("Addition:", c)

d= a - b  # subtraction
print("Subtraction:", d)

e= a * b  # multiplication
print("Multiplication:", e)

f= a / b  # division
print("Division:", f)

# assignment operators
a= 10
# a += 5  # increment a by 5 (equivalent to a = a + 5)
a -= 5 # decrement a by 5 (equivalent to a = a - 5)
print(a)

# comparison operators
a= 10>9
print(a)  # True
b= 10<9
print(b)  # False
c= 10==10
print(c)  # True
d= 10!=10
print(d)  # False
e= 10>=10
print(e)  # True
f= 10<=10
print(f)  # True

# Logical Operators

e = True or False

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(False))  # True