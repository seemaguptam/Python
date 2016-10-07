# 2.08 
maze_start = ["stairs down", "monster", "nothing", "sword", "stairs down", "monster"]
maze_middle = ["nothing", "stairs up", "nothing", "magic crystals", "stairs down", "sword" ]
maze_end = ["PRIZE", "boss monster", "nothing", "nothing", "stairs up", "monster"]
is_alive = True
user_horizontal = 4
user_floor = maze_start
user_pocket = []
won = False
while is_alive and not won:
    user_input = input("What would you like to do? ")
    previous_obstacle = user_floor[user_horizontal]
    print("currently is ", previous_obstacle)
    previous_obstacle_is_monster = previous_obstacle == "monster" or previous_obstacle == "boss monster"
    user_input_is_move = user_input == "right" or user_input == "left" or user_input == "up" or user_input == "down"
    if user_input_is_move and previous_obstacle_is_monster: 
        print("Monster has fatally wounded you :(")
        is_alive = False
    elif user_input == "right":
        user_horizontal+=1
        if user_horizontal < 0 or user_horizontal >= len(user_floor[user_horizontal]):
            print("Sorry can't go that way.")
        else:
            print("You see " + user_floor[user_horizontal])
    elif user_input == "left":
        user_horizontal-=1
        if user_horizontal < 0 or user_horizontal >= len(user_floor[user_horizontal]):
            print("Sorry can't go that way.")
        else:
            print("You see " + user_floor[user_horizontal])
    elif user_input == "up":
        if previous_obstacle != "stairs up" or user_floor == maze_start: 
            print("Cannot go that way.")
        else:
            if user_floor == maze_middle: 
                user_floor = maze_start
            else: 
                user_floor = maze_middle
            print("You see " + user_floor[user_horizontal])
    elif user_input == "down":
        if previous_obstacle != "stairs down" or user_floor == maze_end: 
            print("Cannot go that way.")
        else:
            if user_floor == maze_start: 
                user_floor = maze_middle
            else: 
                user_floor = maze_end
            print("You see " + user_floor[user_horizontal])
    elif user_input == "fight":
        obstacle = user_floor[user_horizontal]
        if obstacle == "boss monster":
            if "sword" in user_pocket and "magic crystals" in user_pocket:
                print("You defeated the boss monster and won!")
                user_pocket.remove("sword")
                user_pocket.remove("magic crystals")
                user_floor[user_horizontal] = "nothing"
                won = True
            elif "magic crystals" in user_pocket:
                print("You wounded the boss monster!")
                user_pocket.remove("magic crystals")
                user_floor[user_horizontal] = "monster"
        elif obstacle == "monster" and  "sword" in user_pocket:
            print("You defeated the monster!")
            user_pocket.remove("sword")
            user_floor[user_horizontal] = "nothing"
        elif obstacle == "monster":
            print("You have been defeated :( ")
            is_alive = False
        else:
            print("You can't fight that!")
    elif user_input == "grab":
        obstacle = user_floor[user_horizontal]
        if obstacle == "sword" or obstacle == "magic crystals":
            print("Picked up " + obstacle)
            user_floor[user_horizontal] = "nothing"
            user_pocket.append(obstacle)
        else:
            print("You can't pick up that!")
    elif user_input == "commands":
        print("Commands are: right, left, up, down, fight, run, grab, and commands")
    elif user_input == "quit": 
        print("You have ended the quest and have lost :(") 
        is_alive = False
    else:
        print("Sorry that input wasn't recognized. Type commands to get all possible commands")
