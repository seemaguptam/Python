# 3.04
import random

my_list = ['a', 'b', 'c', 'd']
# input: a list of strings
# output: None
def my_function(list_argument): 
    list_argument[0] = 'z'
print(my_list)
my_function(my_list)
print(my_list)

def func_int(x):
    x=3
    return x

i=2
func_int(i)
print(i)

def update_list(a_list):
      a_list[3] = "yo"
      b = a_list[4]
      b = 100

my_list = [1, 2, 3, 4, 5]
update_list(my_list)
print(my_list)


# draw stack

var_1 = "kittens"
var_2 = "cookies"

# input: a string
# output: a string
def my_function(my_favorite_things):
      song_lyrics = "rain drops on roses,"
      combined_song = song_lyrics + my_favorite_things
      return combined_song

  # input: a string
  # output: a string
def my_function_2(item, item2):
      full_lyrics = item + " on " + item2
      full_song = my_function(full_lyrics)
      return full_song

my_song = my_function_2(var_1, var_2)
print(my_song)

# from oregon trail
def update_days(low_range, high_range):
	days = random.randint(low_range, high_range)
	print("days is ", days)
	for i in range(0, days):
		print("update current day, month, food_minus and health_minus")

update_days(2,5)

		
