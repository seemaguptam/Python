# 7.02
class Pet(object): 
    """Represents a pet"""
    # {a:'animal', c:'color', f:'food', no:'noise', 'na:'name'}
    def __init__(self, a=0, c=0, f=0, no=0, na=0):
        self.a = a
        self.c = c
        self.f = f
        self.no = no
        self.na = na
    def __str__(self):
         return 'name:food %s:%s' % (self.na, self.f)

my_pet_1 = Pet() 
my_pet_1.a = 'cat'
my_pet_1.no = 'meow'
my_pet_1.na = 'Snuffles McGruff'
my_pet_1.f = 'tuna'

my_pet_2 = Pet()
my_pet_2.a = 'dog'
my_pet_2.no = 'woof'
my_pet_2.na = 'Snowpounce Flury'
my_pet_2.f = 'kibbles'

def get_name_food_info(l):
    for pet in l: 
        print(pet)
   
my_pets = [my_pet_1, my_pet_2]
get_name_food_info(my_pets)
