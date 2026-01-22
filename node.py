from squareshape import SquareState
from enum import Enum
from constants import *



class Node():
    def __init__(self, x, y, distance, state):
        self.x = x
        self.y = y
        self.distance = distance
        self.state = self.set_state(state)
        self.visited = False
        self.grid = "!!!"
        self.neighbours = None
        #print(f"len(self.neighbours: {len(self.neighbours)}")
        self.path = []
        
    class State(Enum):
        NOTHING = 1
        START = 2
        END = 3
        WALL = 4
        VISITED = 5
        CUR_ACTIVE = 6
        CUR_HOVER = 7
        PATH = 8

    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state
        if self.state == Node.State.START:
            self.set_dist(0,self.path)


    def get_pos(self):
        return (self.x, self.y)
    

    def get_dist(self):
        return self.distance
    
    def set_dist(self, dist, path):
        if dist < self.distance:
            self.distance = dist
            if self.state != Node.State.START:
                self.path = path.copy().append(self)
                if self.state != Node.State.END:
                    self.state = Node.State.VISITED
                
                





    def get_neighbours(self):
        x = self.x
        y = self.y

        neighbours:list[Node] = []
        try:
            if x+1 < GRID_SIZE:
                neighbours.append(self.grid[x+1][y])
            if x-1 >= 0:
                neighbours.append(self.grid[x-1][y])
            if y+1 < GRID_SIZE:
                neighbours.append(self.grid[x][y+1])
            if y-1 >= 0:
                neighbours.append(self.grid[x][y-1])
            #print(f"my_pos: {(x,y)} neigbours:{len(neighbours)}")
            return neighbours
        except Exception as e:
            print(f"ERROR: could not add neigbours: {e}| neigbours:{len(neighbours)}")
        

    def set_grid(self, grid):
        self.grid = grid
        self.get_neighbours()

    def visit(self):
        self.visited = True
        return self.state == Node.State.END, self.path
        

    def get_path(self):
        return self.path

    