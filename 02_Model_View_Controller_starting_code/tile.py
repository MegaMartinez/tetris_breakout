# This code written by Matthew Martinez

import pygame
from filesystem import file

blank = pygame.image.load(file("empty/blank.png"))
empty1 = pygame.image.load(file("empty/empty_1.png"))
empty2 = pygame.image.load(file("empty/empty_2.png"))
empty3 = pygame.image.load(file("empty/empty_3.png"))
empty4 = pygame.image.load(file("empty/empty_4.png"))
empty = [empty1, empty2, empty3, empty4]
frame = 0

blue = pygame.image.load(file("block/blue.png"))
green = pygame.image.load(file("block/green.png"))
purple = pygame.image.load(file("block/purple.png"))
orange = pygame.image.load(file("block/orange.png"))
yellow = pygame.image.load(file("block/yellow.png"))
colored = [blue, green, purple, orange, yellow]
colorstr = ["blue", "green", "purple", "orange", "yellow"]


class tile:
    def __init__(self, posx, posy):
        """
        LIST OF VALID STATES:

        0 = blank
        1 = empty
        2 = full
        """
        self.frame = frame
        self.img = blank
        self.state : int = 0
        self.color : str = None
        self.posx = (8 * posx)
        self.posy = (8 * posy)
        self.stophere = False
        self.hitbox = None

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
        self.img = empty[self.frame]
        self.frame += 1

    def fill(self, color):
        self.state = 2
        self.color : str = color
        if self.color in colorstr:
            for k in range(len(colorstr)):
                if colorstr[k] == self.color:
                    self.img = colored[k]
        else:
            errormessage = ('"' + str(color) + '"' + " ISN'T A VALID COLOR")
            raise Exception(errormessage)



    def draw(self, screen):
        screen.blit(self.img, (self.posx, self.posy))

    def updatehitbox(self):
        if self.state == 2:
            self.hitbox = pygame.Rect(self.posx, self.posy, self.img.get_width(), self.img.get_height())

    def checkhit(self, x, y, ball):
        if self.hitbox != None:
            if self.hitbox.collidepoint(x, y):
                self.empty_basic()
                if x <= self.hitbox.x + 1 or x >= self.hitbox.x + self.img.get_width() - 1:
                    ball.bonk_block_side()
                    self.hitbox = None
                # elif x >= self.hitbox.x or x <= self.hitbox.x + self.img.get_width():
                else:
                    ball.bonk_block_top()
                    self.hitbox = None
                if self.color == "blue":
                    pass
                if self.color == "yellow":
                    pass
                if self.color == "orange":
                    pass
                if self.color == "purple":
                    pass
                if self.color == "green":
                    pass



    