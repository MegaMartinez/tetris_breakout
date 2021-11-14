import pygame, sys
import filesystem

class Scoreboard():
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.SysFont(None, 20)

    def draw(self):
        score_string = "{}".format(self.score)
        score_image = self.font.render(score_string, True, (255, 255, 255))
        score_letter = "Score"
        score = self.font.render(score_letter, True, (255, 255, 255))
        self.screen.blit(score_image, (100, 12))
        self.screen.blit(score, (100, 0))
        pygame.draw.line(self.screen, (100, 100, 100), (0, 23), (150, 23))