def check_direction(x, y, x_move, y_move, board, checking):
    while y < len(board) and  x < len(board[y]):
        if board[y][x] != checking:
            return False
        x += x_move
        y += y_move
    return True

def check_side(board, side):
    # check horizontal
    won = False
    for i in range(len(board)):
        won = won or check_direction(0, i, 1, 0, board, side)
        won = won or check_direction(i, 0, 0, 1, board, side)
    won = won or check_direction(0, 0, 1, 1, board, side)
    won = won or check_direction(0, len(board)-1, 1, -1, board, side)
    return won

def tic_tac_toe_checker(board, x_name, y_name):
    right_side_won = check_side(board, 'x')
    if right_side_won:
        print(x_name +  " won")
        return True
    else:
        left_side_won = check_side(board, "o")
        if left_side_won:
            print(y_name + " won")
            return True
        else:
            return False

def make_move(board, player, x, y): 
    if y > len(board)-1  or x > len(board[y]) -1 : 
        print("Cannot go there. Not on board")
        return False
    elif board[y][x] != ' ': 
        print("That spot is not open")
        return False
    elif player == 'x': 
        board[y][x] = 'x'
        return True
    else: 
        board[y][x] = 'o'
        return True

def print_board(board): 
    for column_index in range(0, len(board)): 
        row = " "
        for row_index in range(0, len(board[column_index])): 
            if row_index != len(board[column_index]) -1 : 
                row += board[column_index][row_index] + " |"
            else: 
                row += board[column_index][row_index]
        print(row)
        if column_index !=len(board) -1: 
            print("----------")

def game_loop(): 
    print("Welcome to tic-tac-toe. x's go first")
    x_name = input("What is your name x?")
    y_name = input("What is your name o?")
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    turn = 'x'
    while not tic_tac_toe_checker(board, x_name, y_name): 
        print_board(board)
        if turn == 'x': 
            greeting = x_name 
        else: 
            greeting = y_name
        user_x = input(greeting + " which column would you like? ")
        user_y = input(greeting + " which row would you like? ")
        if user_x == "quit" or user_y == "quit": 
            return
        could_move = make_move(board, turn, int(user_x), int(user_y))
        if could_move: 
            if turn == 'x': 
                turn = 'o'
            else: 
                turn = 'x'
            
game_loop()
