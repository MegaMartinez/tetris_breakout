import pygame

class powerup:
    def __init__(self, color, posx, posy):
        """
        0 = blue (bomb)
        1 = green (score)
        2 = orange (slightly faster paddle)
        3 = purple (slow)
        4 = yellow (long)
        """
        self.type = ["blue", "green", "orange", "purple", "yellow"].index(color)
        self.x = posx
        self.y = posy
    
    def activate(self):
        if self.type == 0:
            pass
        if self.type == 1:
            pass
        if self.type == 2:
            pass
        if self.type == 3:
            pass
        if self.type == 4:
            pass