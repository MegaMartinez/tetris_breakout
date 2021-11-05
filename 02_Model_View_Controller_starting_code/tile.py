import pygame
from filesystem import file

blank = pygame.image.load(file("empty/blank.png"))
empty1 = pygame.image.load(file("empty/empty_1.png"))
empty2 = pygame.image.load(file("empty/empty_2.png"))
empty3 = pygame.image.load(file("empty/empty_3.png"))
empty4 = pygame.image.load(file("empty/empty_4.png"))


class tile:
    def __init__(self, posx, posy):
        """
        LIST OF VALID STATES:

        0 = blank
        1 = empty
        2 = full
        """
        
        self.img = blank
        self.state : int = 0
        self.color : str = None
        self.posx = (8 * posx)
        self.posy = (8 * posy)

    def blank(self):
        self.state = 0
        self.color : str = None

    def empty_basic(self):
        self.state = 1
        self.color : str = None
        self.img = empty4
    
    def empty_anim(self):
        self.state = 1
        self.color : str = None
        self.img = empty1

    def fill(self, color):
        self.state = 2
        self.color : str = color

    def draw(self, screen):
        screen.blit(self.img, (self.posx, self.posy))

