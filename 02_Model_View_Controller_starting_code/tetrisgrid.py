import pygame
from tile import tile

class tetrisgrid:
    def __init__(self):
        """
        FOR ANYONE WORKING WITH THIS GRID

        The list stores certain spots on the grid by rows and then columns of each row
        So to call a specific cell, you need to call it as:
        self.row[y][x]
        To get cell (x, y)

        Also keep in mind that both lists index from 0
        """

        row = []
        column = []
        for ky in range(20):
            for kx in range(10):
                column += [tile()]
            row += [column]
            column = []
        self.row = row


