import pygame
from enum import Enum

class SquareShape(pygame.sprite.Sprite):
    def __init__(self, x, y , size):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.size = size

    def draw(self, screen):

        pass
    def update(self, screen):

        pass

class SquareState(Enum):
    NOTHING = 1
    START = 2
    END = 3
    WALL = 4
    SEARCHED = 5
    CUR_ACTIVE = 6