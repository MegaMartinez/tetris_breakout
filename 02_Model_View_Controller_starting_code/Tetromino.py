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

valid = ["I", "J", "L", "O", "T", "S", "Z"]
# the following lists will be ordered relatively the same as the one just above
colors = ["blue", "red", "red", "yellow", "purple", "green", "green"]

class Tetromino:
    def __init__(self, shape):
        if shape is not str or shape not in valid:
            errormessage = ('"' + str(shape) + '"' + " is not a valid shape.")
            raise Exception(errormessage)
        self.shape = shape
        shapeindex = valid.index(shape)
        self.color = colors[shapeindex]
        