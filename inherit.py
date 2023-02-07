class Animal:
    def __init__(self, name, age) -> None:
        self.name= name
        self.age= age
    
    def show(self):
        print(f"I am {self.name}  my age is {self.age}")
    
    def speak(self):
        print("I cant speak")
    
class Dog(Animal):
    def speak(self):
        print("bark")

class Fish(Animal):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self.color =color
    def show(self):
        print(f"I am {self.name} age{self.age} my color is {self.color}")

d= Dog("tim", 5)
d.show()
d.speak()
f= Fish("mim", 2,"Brown")
f.show()
f.speak()