import pygame
from constants import *

from node import Node


clock = pygame.time.Clock()
dt = 0


is_drawing = False
is_erasing = False
last_hover = (0, 0)

def main():
    
    global grid
    grid = create_grid()
    
    #print(grid)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #GAME LOOP_________________________________________________________________________________________________________
    while True:
        exit = check_input_events()
        if exit:
            return
        
        cur_mouse_pos = get_mouse_to_grid_pos()
        check_hover_square(cur_mouse_pos)

        if is_drawing:
            create_wall(cur_mouse_pos)
        elif is_erasing:
            erase_square(cur_mouse_pos)
        

        screen.fill("black")
        
        for j in range(GRID_SIZE):
            for i in range(GRID_SIZE):
                cur_color = "white"
                my_rect = pygame.Rect(LINE_SIZE+(RECT_SIZE+LINE_SIZE)*i,LINE_SIZE+(RECT_SIZE+LINE_SIZE)*j,RECT_SIZE,RECT_SIZE)
                #print(type(grid[i][j]))
                cur_state = grid[i][j].get_state()
                match cur_state:
                    case Node.State.WALL:
                        cur_color = "black"
                    case Node.State.CUR_HOVER:
                        cur_color = HOVER_COLOR
                    case Node.State.START:
                        cur_color = START_COLOR
                    case Node.State.END:
                        cur_color = END_COLOR

                pygame.draw.rect(screen,cur_color,my_rect)
        pygame.display.flip()
        

        dt = clock.tick(60)/ 1000
        #print(dt)
        







def check_input_events():
    global is_drawing
    global is_erasing
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            is_drawing = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            is_drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            is_erasing = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            is_erasing = False


def check_hover_square(pos):
    global last_hover
    last_state = grid[last_hover[0]][last_hover[1]].get_state()
    cur_state = grid[pos[0]][pos[1]].get_state()
    #print(pos[0],pos[1])
    if cur_state == Node.State.NOTHING:
        grid[pos[0]][pos[1]].set_state(Node.State.CUR_HOVER)
    if pos != last_hover and last_state == Node.State.CUR_HOVER:
        grid[last_hover[0]][last_hover[1]].set_state(Node.State.NOTHING)
    last_hover = pos



def create_start(pos):
    global grid
    grid[pos[0]][pos[1]].set_state(Node.State.START)

def erase_square(pos):
    global grid
    cur_state = grid[pos[0]][pos[1]].get_state()
    if cur_state == Node.State.WALL:
        grid[pos[0]][pos[1]].set_state(Node.State.NOTHING)

def create_wall(pos):
    global grid
    cur_state = grid[pos[0]][pos[1]].get_state()
    if cur_state != Node.State.START and cur_state != Node.State.END:
        grid[pos[0]][pos[1]].set_state(Node.State.WALL)

def get_mouse_to_grid_pos():
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    #print((x,y))   
    grid_pos = (min(x//(RECT_SIZE+LINE_SIZE),GRID_SIZE-1), min(y//(RECT_SIZE+LINE_SIZE),GRID_SIZE-1))
    grid_pos = (max(grid_pos[0],0), max(grid_pos[1],0))
   
    if grid_pos[0] < 0 or grid_pos[1] < 0:
        print(grid_pos)
    return grid_pos


def create_grid():
    arr = [[Node(i,j,float('inf'),Node.State.NOTHING) for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
    arr[10][2].set_state(Node.State.START)
    arr[GRID_SIZE-6][GRID_SIZE-5].set_state(Node.State.END)
    return arr


    
if __name__ == "__main__":
    main()
