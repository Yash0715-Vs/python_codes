def greet():
    print("hello")

class student:
    def __init__(self,name):#it is dunder method which is auto call (constructor)
        self.name= name
    def display(self):
        print(self.name)

if __name__ == "__main__":
    print("Running as Script")

