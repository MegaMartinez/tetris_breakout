import pygame
import time

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
        self.x = posx + 4
        self.y = posy + 4
        self.time_since_last = 0
        self.color = color
        # self.object = pygame.draw.circle(screen, color, (posx, posy), 2)

    def move(self):
        self.x -= 1

    def activate(self, game):
        if self.type == 0:
            pass
        if self.type == 1:
            pass
        if self.type == 2:
            pass
        if self.type == 3:
            pass
        if self.type == 4:
            game.paddle.long_paddle()
            if time.time() - self.time_since_last < 10.0:
                game.paddle.short_paddle()
            pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 4)
