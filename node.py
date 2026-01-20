from squareshape import SquareState
from enum import Enum


class Node():
    def __init__(self, x, y, distance ,state):
        self.x = x
        self.y = y
        self.distance = distance
        self.state = state

    class State(Enum):
        NOTHING = 1
        START = 2
        END = 3
        WALL = 4
        SEARCHED = 5
        CUR_ACTIVE = 6
        CUR_HOVER = 7

    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state

    def get_neighbours(self):
        pass

    def change_dist(self, new_dist):
        self.distance = new_dist