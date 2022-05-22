import time


GAME_SPEED = 1
GRID_SIZE = 12



#depending on direction snake is going to go, make head look like ^, v, <, >. Make body # and sneak food *
SNAKE_HEAD_LOCATION = 5
SNAKE_HEAD_DIRECTION = '>'  #[^, v, <, >]
SNEAK_BODY_LOCATION = [4,3,2]
FOOD_LOCATION = 54




#launch game






#while game is not crashed, main loop
def main():

    while True:


        draw_board()




        time.sleep(GAME_SPEED)

    #close game







def draw_board():
    print(' '+'__'*GRID_SIZE)

    for i in range(GRID_SIZE-1):
        print('|'+' '*GRID_SIZE*2+'|')

    print('|'+'__'*GRID_SIZE+'|')


    #replace spaces with snek
    

    #replaces spaces with snek food





main()