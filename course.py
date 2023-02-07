class Animal:
    def __init__(self, name, age) -> None:
        self.name= name
        self.age = age
    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")
    
    def speak(self):
        print("i cant speak")

class Dog(Animal):
    def speak(self):
        print("bark")

class Cat(Animal):
    def speak(self):
        print("meow")
class Fish(Animal):
    pass
p= Animal("mill", 3)   
p.show() 
p.speak()
d= Dog("sam",5)
d.show()
d.speak()
c= Cat("pam",4)
c.show()
c.speak()
f= Fish("bob",1)
f.show()
f.speak()