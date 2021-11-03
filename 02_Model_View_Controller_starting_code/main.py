import pygame
from pygame.constants import FULLSCREEN, SCALED
from Game import Game
from Controller import Controller
from View import View

# TODO: Put your names here (entire team)


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 375))  # TODO: Choose your own size
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller

    frame_rate = 60  # TODO: Choose your own frame rate

    i = 0

    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_one_cycle()
       # viewer.draw_everything()
        if i == 0:
            game.draw_once()
        i += 1



main()
