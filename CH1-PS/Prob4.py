import os

# Specify the directory path
path = "/"

# Get the list of files and folders
contents = os.listdir(path)

# Print the contents
print("Contents of the directory are:")
for item in contents:
    print(item)