import pygame
import sys
from Game import Game

# TODO: Put your names here (entire team)


class Controller:
    def __init__(self, game: Game):
        self.game = game
        self.runonce = 0

    def get_and_handle_events(self):
        """
        [Describe what keys and/or mouse actions cause the game to ...]
        """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_ESCAPE]:
            pygame.quit()
        
        # These keys are purely for debug. REMEMBER TO DELETE THEM LATER
        if pressed_keys[pygame.K_u]:
            if self.runonce == 0:
                self.game.emptyanimation = True
            self.runonce = 1
        
        if pressed_keys[pygame.K_f]:
            if self.runonce == 0:
                self.game.spawntetromino()
            self.runonce = 1

        if pressed_keys[pygame.K_RSHIFT]:
            self.runonce = 0

        if pressed_keys[pygame.K_LSHIFT]:
            if self.runonce == 0:
                self.game.tetrisgrid.checkrow()
            self.runonce = 1

        if pressed_keys[pygame.K_s]:
            if self.runonce == 0 and self.game.tetromino != None:
                self.game.tetromino.movedown()
            self.runonce = 1

        if pressed_keys[pygame.K_a]:
            if self.runonce == 0 and self.game.tetromino != None:
                self.game.tetromino.movehorizontal(-8)
            self.runonce = 1
        
        if pressed_keys[pygame.K_d]:
            if self.runonce == 0 and self.game.tetromino != None:
                self.game.tetromino.movehorizontal(8)
            self.runonce = 1

        # Use code like the following, but for YOUR Game object.
        #     if pressed_keys[pygame.K_LEFT]:
        #         self.game.fighter.move_left()
        #     if pressed_keys[pygame.K_RIGHT]:
        #         self.game.fighter.move_right()
        #
        #     if self.key_was_pressed_on_this_cycle(pygame.K_SPACE, events):
        #         self.game.fighter.fire()

    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    @staticmethod
    def key_was_pressed_on_this_cycle(key, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
