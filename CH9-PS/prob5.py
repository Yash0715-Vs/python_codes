words =["Yash","sahil","preet"]

with open ("file.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "Suthar" *len(word))

with open ("file.txt", "w") as f:
    f.write(content)