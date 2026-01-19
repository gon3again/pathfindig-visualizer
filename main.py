import pygame
from constants import *
from squareshape import SquareState

clock = pygame.time.Clock()
dt = 0

is_drawing = False



def main():
    global is_drawing
    global grid
    grid = create_grid()
    grid[1][1] = "black"
    print(grid)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                is_drawing = False

        if is_drawing:
            create_wall(get_mouse_to_grid_pos())
        

        screen.fill("black")
        
        for j in range(GRID_SIZE):
            for i in range(GRID_SIZE):
                cur_color = "white"
                my_rect = pygame.Rect(LINE_SIZE+(RECT_SIZE+LINE_SIZE)*i,LINE_SIZE+(RECT_SIZE+LINE_SIZE)*j,RECT_SIZE,RECT_SIZE)
                if grid[i][j] == SquareState.WALL:
                    cur_color = "black"
                pygame.draw.rect(screen,cur_color,my_rect)
        pygame.display.flip()
        

        dt = clock.tick(60)/ 1000
        #print(dt)
        


    print(f"_____________{pygame.version.ver}")




def create_wall(pos):
    global grid
    grid[pos[0]][pos[1]] = SquareState.WALL

def get_mouse_to_grid_pos():
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    print((x,y))   
    grid_pos = (x//(LINE_SIZE+(RECT_SIZE+LINE_SIZE)), y//(LINE_SIZE+(RECT_SIZE+LINE_SIZE)))
    return grid_pos


def create_grid():
    arr = [[SquareState.NOTHING for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
    return arr
    
if __name__ == "__main__":
    main()
