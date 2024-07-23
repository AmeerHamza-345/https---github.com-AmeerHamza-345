class MyClass2:
    def __init__(self, name): 
        self.name = name
obj = MyClass2("Ameer Hamza")
print(obj.name)

class Person:
    def __init__(self, name, age, height):
        self.name = name    # شخص کا نام
        self.age = age   
        self.height = height
        self.jump = height

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Height:{self.height}, Can jump up to:{self.jump}")


person1 = Person("علی", 25, 5)
person2 = Person("سارا", 30, 4)


person1.display_info()  
person2.display_info()

