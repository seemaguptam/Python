# Lab 2.04, Problem 3 
prize_1 = "Goat"
prize_2 = "$100"
prize_3 = "Goat"
prize_4 = "Goat"
prize_5 = "Goat"
prize_6 = "$1,000,000"
prize_7 = "Goat"
prize_8 = "Goat"
prize_9 = "Goat"
prize_10 = "$1"

user_number = input("What door number do you want? ")

if user_number == "1": 
	print("You get a " + prize_1)
elif user_number == "2": 
	print("You get a " + prize_2)
elif user_number == "3": 
	print("You get a " + prize_3)
elif user_number == "4": 
	print("You get a " + prize_4)
elif user_number == "5": 
	print("You get a " + prize_5)
elif user_number == "6": 
	print("You get a " + prize_6)
elif user_number == "7": 
	print("You get a " + prize_7)
elif user_number == "8": 
	print("You get a " + prize_8)
elif user_number == "9": 
	print("You get a " + prize_9)
elif user_number == "10": 
	print("You get a " + prize_10)
else: 
	print("Incorrect input, you get nothing!")
	
