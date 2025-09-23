class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        base_sound = super().speak()   # odwołanie do metody rodzica
        return base_sound + " + Woof!"

dog = Dog()
print(dog.speak())  # Some sound + Woof!