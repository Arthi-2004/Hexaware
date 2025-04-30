from entity.pet import Pet

class Cat(Pet):
    def __init__(self, name, age, breed, cat_color):
        super().__init__(name, age, breed)
        self._cat_color = cat_color

    def get_cat_color(self):
        return self._cat_color

    def set_cat_color(self, cat_color):
        self._cat_color = cat_color

    def __str__(self):
        return f"Cat [Name: {self.get_name()}, Age: {self.get_age()}, Breed: {self.get_breed()}, Color: {self._cat_color}]"
