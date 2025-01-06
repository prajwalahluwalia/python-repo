class Animal:
    def speak(self):
        return f"Animal makes noises."
    
class Dog(Animal):
    def speak(self):
        return "Woof"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
animal = Animal()
print(animal.speak())

dog = Dog()
print(dog.speak())

cat = Cat()
print(cat.speak()   )