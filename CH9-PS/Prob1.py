f=open("file.txt","r")
content=f.read()
print(content)
if ("blue" in content):
    print("The word 'blue' is present in the file.")
else:
    print("The word 'blue' is not present in the file.")

f.close()