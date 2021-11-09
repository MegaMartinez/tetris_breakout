# This code written by Matthew Martinez

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
                column += [tile(kx + 8, ky + 3)]
            row += [column]
            column = []
        self.row = row
    
    def clear_next_frame(self):
        for ky in range(20):
            for kx in range(10):
                self.row[ky][kx].empty_anim()

    def fill(self, cellx, celly, color):
        self.row[celly][cellx].fill(color)

    def get_stopspots(self):
        final = []
        for ky in range(20):
            for kx in range(10):
                if self.row[ky][kx].stophere == True:
                    final += [[self.row[ky][kx].posx, self.row[ky][kx].posy]]
        return final

    def debugfill(self, color):
        # will delete later
        # srsly please remind me to delete this it's completely useless
        pass
    
    def checkrow(self):
        for ky in range(20):
            countfilled = 0
            for kx in range(10):
                if self.row[ky][kx].state == 2:
                    countfilled += 1
            if countfilled == 10:
                for kx in range(10):
                        self.row[ky][kx].empty_basic()
        for ky in range(19, -1, -1):
            # this will check if it's empty
            countempty = 0
            for kx in range(10):
                if self.row[ky][kx].state == 1:
                    countempty += 1
            if countempty == 10:
                # this will find nearest row with a filled block
                nearest = 0
                for ky2 in range(ky, -1, -1):
                    for kx2 in range(10):
                        if self.row[ky2][kx2].state == 2:
                            nearest = ky2
                    if nearest == ky2:
                        break
                for kx in range(10):
                    if self.row[ky2][kx].state == 2:
                        self.row[ky][kx].fill(self.row[ky2][kx].color)
                    self.row[ky2][kx].empty_basic()
    
    def updatestops(self):
        for ky in range(20):
            for kx in range(10):
                if self.row[ky][kx].state == 2:
                    self.row[ky - 1][kx].stophere = True
        for kx in range(10):
            self.row[19][kx].stophere = True
                        
        
                    

