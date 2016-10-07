#3.02
import random
number = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

def my_func(lis):
    i=0
    while (i<5):
        s1=random.choice(number)
        s2=random.choice(suit)
        lis.append([s1,s2])
        i+=1
    return(lis)

lis=[]
lis2=my_func(lis)
print(lis2)
