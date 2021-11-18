import pygame
from Scoreboard import Scoreboard
import math

class Start:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 15)

    def draw(self, first, second, third):
        score_string1 = "1. " + "{}".format(first)
        score_string2 = "2. " + "{}".format(second)
        score_string3 = "3. " + "{}".format(third)
        score_letter = "Highscore Board"
        score_image1 = self.font.render(score_string1, True, (255, 255, 255))
        score_image2 = self.font.render(score_string2, True, (255, 255, 255))
        score_image3 = self.font.render(score_string3, True, (255, 255, 255))
        score = self.font.render(score_letter, True, (255, 255, 255))
        self.screen.blit(score_image1, (100, 30))
        self.screen.blit(score_image2, (100, 50))
        self.screen.blit(score_image3, (100, 70))
        self.screen.blit(score, (100, 15))

