import pygame

img = pygame.image.load("02_Model_View_Controller_starting_code/test_pixel.png")

class tile:
    def __init__(self, posx, posy, screen):
        """
        LIST OF VALID STATES:

        0 = blank
        1 = empty
        2 = full
        """
        
        self.state : int = 0
        self.color : str = None
        self.posx = -250 + ((16 * posx) + 144)
        self.posy = -187 + ((16 * posy) + 64)

    def blank(self):
        self.state = 0
        self.color : str = None

    def empty(self):
        self.state = 1
        self.color : str = None
        for k in range(8):
            pass

    def fill(self, color):
        self.state = 2
        self.color : str = color

    def draw(self, screen):
        screen.blit(img, (self.posx, self.posy))
        pygame.display.update()