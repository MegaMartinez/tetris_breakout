#------------------------------------------------------------------------#
# FUN FACT: THE BLOCK SHAPES IN TETRIS ARE CANONICALLY CALLED TETROMINOS #
#------------------------------------------------------------------------#
# This code written by Matthew Martinez


#-----------------------------#
# A GUIDE TO TETROMINO SHAPES #
#-----------------------------#

"""
                    I
    _   0   _   
    _   0   _   
    _   0   _   
    _   0   _   
                    
                    J 
    _   _   _   
    _   0   _   
    _   0   _   
    0   0   _   

                    L
    _   _   _   
    _   0   _   
    _   0   _   
    _   0   0   

                    O
    _   _   _   
    _   0   0   
    _   0   0   
    _   _   _   

                    T
    _   _   _   
    _   0   _   
    0   0   0   
    _   _   _   

                    S
    _   _   _   
    _   0   0   
    0   0   _   
    _   _   _   

                    Z
    _   _   _   
    0   0   _   
    _   0   0   
    _   _   _   
"""

import pygame
from filesystem import file

blue = pygame.image.load(file("block/blue.png"))
green = pygame.image.load(file("block/green.png"))
purple = pygame.image.load(file("block/purple.png"))
orange = pygame.image.load(file("block/orange.png"))
yellow = pygame.image.load(file("block/yellow.png"))

valid = ["I", "J", "L", "O", "T", "S", "Z"]
# the following lists will be ordered relatively the same as the one just above
colors = [blue, orange, orange, yellow, purple, green, green]
colornames = ["blue", "orange", "orange", "yellow", "purple", "green", "green"]
block2offset = [[-8, 0], [-8, 0], [-8, 0], [8, 0], [-8, 0], [0, 8], [-8, 0]]
block3offset = [[8, 0], [8, 0], [8, 0], [8, 8], [8, 0], [-8, 8], [8, 8]]
block4offset = [[16, 0], [8, 8], [-8, 8], [0, 8], [0, 8], [8, 0], [0, 8]]


class Tetromino:
    def __init__(self, shape):
        if type(shape) != str or shape not in valid:
            errormessage = ('"' + str(shape) + '"' + " is not a valid shape.")
            raise Exception(errormessage)
        self.shape = shape
        shapeindex = valid.index(shape)
        self.img = colors[shapeindex]
        self.color = colornames[shapeindex]
        self.startposition = [(12 * 8), (3 * 8)]
        self.block2position = [((12 * 8) + block2offset[shapeindex][0]), ((3 * 8) + block2offset[shapeindex][1])]
        self.block3position = [((12 * 8) + block3offset[shapeindex][0]), ((3 * 8) + block3offset[shapeindex][1])]
        self.block4position = [((12 * 8) + block4offset[shapeindex][0]), ((3 * 8) + block4offset[shapeindex][1])]
        self.positions = [self.startposition, self.block2position, self.block3position, self.block4position]

    def movehorizontal(self, dir):
        self.startposition[0] += dir
        self.block2position[0] += dir
        self.block3position[0] += dir
        self.block4position[0] += dir

    def movedown(self):
        self.startposition[1] += 8
        self.block2position[1] += 8
        self.block3position[1] += 8
        self.block4position[1] += 8

    def draw(self, screen):
        screen.blit(self.img, (self.startposition))
        screen.blit(self.img, (self.block2position))
        screen.blit(self.img, (self.block3position))
        screen.blit(self.img, (self.block4position))
