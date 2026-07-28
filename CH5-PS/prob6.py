s={}
name = input("Enter your 1stname: ")
language = input("Enter your favorite programming language: ")
s[name] = language
name = input("Enter your 2nd name: ")
language = input("Enter your favorite programming language: ")
s[name] = language
name = input("Enter your 3rd name: ")
language = input("Enter your favorite programming language: ")
s[name] = language #this will add the name and language to the dictionary
s.update(s) # update the dictionary with itself
name = input("Enter your 4th name: ")
language = input("Enter your favorite programming language: ")
s[name] = language

print(s)
