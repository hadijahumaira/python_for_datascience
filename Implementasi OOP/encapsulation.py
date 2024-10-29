class Animal:
    def __init__(self, name, species):
        self._name = name            # Protected attribute
        self.__species = species     # Private attribute

    @property
    def species(self):
        return self.__species        # Getter for private attribute

    @species.setter
    def species(self, species):
        if species in ["Kucing", "Anjing", "Burung"]:
            self.__species = species  # Set new species
        else:
            raise ValueError("Spesies tidak valid.")  # Raise error for invalid species

# Menggunakan kelas Animal
if __name__ == "__main__":
    my_animal = Animal("Charlie", "Kucing")
    print(my_animal.species)  # Mengakses species: Kucing

    my_animal.species = "Anjing"  # Menggunakan setter untuk mengatur species
    print(my_animal.species)  # Sekarang species: Anjing
