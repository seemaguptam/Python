#7.04

class Pet(object): 
    def __init__(self, name='default'): 
        self.name = name

    def make_noise(self): 
        print("Noise!")
        return 

class Dog(Pet): 
    """
    A specific type of Pet! 
    """

dog1 = Dog()
dog1.make_noise()

class Pokemon():
    def growl(self):
        print("pokemon")

class Water_Type(Pokemon):
    def spalsh(self):
        print("Splish Splosh")

class Fire_Type(Pokemon):
    def growl(self):
        print("Fire Fire")

class Grass_Type(Pokemon):
    def growl(self):
        print("Cheep Cheep")

wt = Water_Type()
ft = Fire_Type()
gt = Grass_Type()

wt.growl()
ft.growl()
gt.growl()

print(isinstance(wt, Pokemon))  # returns true
print(isinstance(wt, Water_Type))  # returns true

pk= Pokemon()
print(isinstance(pk, Pokemon))  # returns true
print(isinstance(pk, Water_Type)) # returns false

my_pet = Pet()
print(isinstance(my_pet, Pet)) # returns true
print(isinstance(my_pet, Dog)) # returns false

