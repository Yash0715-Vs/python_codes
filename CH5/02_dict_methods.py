marks = {
    "yash": 100,
    "yash1": 56,
    "yash2": 23,
   
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"yash": 99, "Renuka": 100})
# print(marks)

# print(marks.get("yash2")) # Prints None
# print(marks["yash2"]) # Returns an error because the key is not present in the dictionary
# print(marks.clear()) # Clears the dictionary
# print(marks.pop("yash1")) # Removes the key-value pair with the specified key
print(marks.popitem()) # Removes and returns the last key-value pair added to the dictionary
# print(marks.setdefault("yash3", 50)) # Adds a new key-value pair if the key is not present, otherwise returns the value of the existing key
# print(marks)