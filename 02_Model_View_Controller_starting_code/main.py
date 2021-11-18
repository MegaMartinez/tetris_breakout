import pygame
from pygame.constants import FULLSCREEN, SCALED
from Game import Game
from Controller import Controller
from View import View

# Maddie Fletcher, Luca Acquasaliente, Matthew Martinez


def main():
    pygame.init()
    screen = pygame.display.set_mode((184, 184), SCALED)
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller

    frame_rate = 60


    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_one_cycle()
        viewer.draw_everything()


main()
