# 3.03
import random


deck=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
deck=deck*4


# you could just do random.shuffle(deck) instead of using a function
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


#player_turn: takes in a player name, player_name, and draws/removes a card from the deck,
#prints "user drew card x", and returns the value
#input: player_name, string
#output: string - if deck empty reeturn zero
def player_turn(name):
    x=0
    if (len(deck) != 0):
        x = random.choice(deck)
        deck.remove(x)
        print(name + " drew ", x)
    else:
        print("deck is empty")
    return x


# player compare
# tbd

def play(deck):
    p1_score=0
    p2_score=0
    while (len(deck) != 0):
        s1=player_turn("p1")
        s2=player_turn("p2")
        p1_score += int(s1)
        p2_score += int(s2)

    print("p1_score is ", p1_score)
    print("p2_score is ", p2_score)

    if (p1_score > p2_score):
        print("player 1 won")
    elif (p2_score > p1_score):
        print("player 2 won")
    else:
        print("ganme was a draw")

deck=shuffle_deck(deck)
print(deck)
play(deck)

answer = input("do you want to play again")
if (answer == 'yes'):
    deck=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    deck=deck*4
    deck=shuffle_deck(deck)
    print(deck)
    play(deck)
else:
    print("thanks for playing")

   
    
    
