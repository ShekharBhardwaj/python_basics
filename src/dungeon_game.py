import random
import os

#draw a grid
#pick a random location for a player 
#pick a random location for the door 
#pick a random location for the monster
#draw the player in the grid 
#take the input from the player 
#move the player, unless invalid move 
#check for win or loss 
#clear the screen and redraw the grid

CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
         (0,1), (1,1), (2,1), (3,1), (4,1),
         (0,2), (1,2), (2,2), (3,2), (4,2),
         (0,3), (1,3), (2,3), (3,3), (4,3),
         (0,4), (1,4), (2,4), (3,4), (4,4)]

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def random_tuple():
    low = 0
    high = 4
    return [ ( random.randint(low, high), random.randint(low, high) )]

def get_locations():
    return random.sample(CELLS, 3)

def move_player(player, move):
    x,y = player
    
    #if move == LEFT, x-1
    #if move == RIGHT, x+1
    #if move == UP, y-1
    #if move == DOWN, y+1
    
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    if move == "XUPRIGHT":
        x +=1
        y -=1
    if move == "XDOWNRIGHT":
        x +=1
        y +=1
    if move == "XUPLEFT":
        x -=1
        y -=1
    if move == "XDOWNLEFT":
        x -=1
        y +=1

    return (x,y)

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN", "XUPRIGHT", "XDOWNRIGHT", "XDOWNLEFT", "XUPLEFT"]
    
    x,y = player
         
    #if player y == 0 can't move up
    #if player y == 4 can't move down
    #if player x == 0 can't move left
    #if player x == 4 can't move right 
    
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    if x == 0 or y == 0:
        moves.remove("XUPLEFT")
    if x == 0 or y == 4:
        moves.remove("XDOWNLEFT")
    if x == 4 or y == 0:
        moves.remove("XUPRIGHT")
    if x == 4 or y == 4:
        moves.remove("XDOWNRIGHT")
    
    return moves

def monster_or_door(player, monster, door):
    continue_game = True
    if player == monster:
        print("YOU LOSE! Monster got you ! ಥ_ಥ")
        continue_game = False
    elif player == door:
        print("YOU WIN! You are free, you found the way out ! ᕙ(⇀‸↼‶)ᕗ ")
        continue_game = False
    return continue_game
 

def draw_map(player, monster,door, isDebug):
   
    print(" _"*5)
    tile  = "|{}"
    for cell in CELLS:
        x,y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            elif isDebug == "debug" and cell == monster:
                output = tile.format("@")
            elif isDebug == "debug" and cell == door:
                output = tile.format("#")
            else:
                output = tile.format("_")
        else:
            line_end = '\n'
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)
    
def game_loop(isdebug):
    #Good move? change the player position
    #Bad move? Don't change anything!
    #On the door? they win!
    #On the monster? They lose!
    #Otherwise, loop back around
    ref_moves = ["LEFT", "RIGHT", "UP", "DOWN", "XUPRIGHT", "XDOWNRIGHT", "XDOWNLEFT", "XUPLEFT"]
    monster, door, player = get_locations()
    playing = True
    while playing:
        clear_screen()
        draw_map(player, monster, door, isdebug)
        valid_moves = get_moves(player)
        print("You're currently in room {}".format(player)) #fill with location 
        print("You can move {}".format(",".join(valid_moves))) # fill with available moves
        print("Enter QUIT to quit")
        move = input(">").upper()
        if move == "QUIT":
            print("See you around ... muhahahahahaha")
            break
        if move in valid_moves:
            player = move_player(player, move)
            playing = monster_or_door(player, monster, door)
        else:
            if move in ref_moves:
                input("\n ** Walls of my dungeon is unbreakable muahahahaha ! ** \n")
            else:
                input(("\n **You scared you fat fingered the keys, {} is not a valid move  muahahahaha !** \n").format(move))        
    else:
        if input("Do you wanna challenge the monster again ? Y/n ").upper() != "N":
            main_fn()
        else:
            print("See you around ... muhahahahahaha")
    
def main_fn():
    clear_screen()
    print("Welcome to the dungeon!")
    isdebug = input("Press return to start.." or "notdebug").lower()
    clear_screen()
    game_loop(isdebug)
    
    
main_fn()
    
    