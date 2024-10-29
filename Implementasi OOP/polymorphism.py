# polymorphism.py
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Suara tidak dikenal"

    def info(self):
        return f"Hewan ini bernama {self.name}"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Dog(Animal):
    def sound(self):
        return "Woof!"

# Polymorphism Example
def animal_sound(animal):
    print(f"{animal.name}: {animal.sound()}")

if __name__ == "__main__":
    cat = Cat("Luna")
    dog = Dog("Max")
    
    animal_sound(cat)  # Luna: Meow!
    animal_sound(dog)  # Max: Woof!
