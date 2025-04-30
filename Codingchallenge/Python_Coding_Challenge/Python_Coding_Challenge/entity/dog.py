from entity.pet import Pet

class Dog(Pet):
    def __init__(self, name, age, breed, dog_breed):
        super().__init__(name, age, breed)
        self._dog_breed = dog_breed

    def get_dog_breed(self):
        return self._dog_breed

    def set_dog_breed(self, dog_breed):
        self._dog_breed = dog_breed

    def __str__(self):
        return f"Dog [Name: {self.get_name()}, Age: {self.get_age()}, Breed: {self.get_breed()}, Dog Breed: {self._dog_breed}]"
