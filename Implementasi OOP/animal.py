class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Method ini harus diimplementasikan di subclass")

    def info(self):
        return f"Hewan ini bernama {self.name}"

class Mammal(Animal):
    def __init__(self, name, leg_count):
        super().__init__(name)  # Menggunakan super untuk memanggil constructor dari superclass
        self.leg_count = leg_count

    def info(self):
        return f"{self.name} adalah mamalia dengan {self.leg_count} kaki."

class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name, 4)  # Menggunakan 4 sebagai jumlah kaki untuk Dog
        self.breed = breed

    def sound(self):
        return "Woof!"

    def info(self):
        return f"{self.name} adalah anjing ras {self.breed} dengan {self.leg_count} kaki."

# Invoke Example
if __name__ == "__main__":
    my_dog = Dog("Buddy", "Labrador")
    print(my_dog.info())  # Buddy adalah anjing ras Labrador dengan 4 kaki.
    print(my_dog.sound())  # Woof!
