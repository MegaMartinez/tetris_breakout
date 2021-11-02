import pygame

class tile:
    def __init__(self):
        self.empty : bool = True
        self.color : str = None

    def fill(self, color):
        self.empty = False
        self.color : str = color

    def clear(self):
        self.empty = True
        self.color : str = None

