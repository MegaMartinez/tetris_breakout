import pygame
import sys
from Game import Game

# Maddie Fletcher, Luca Acquasaliente, Matthew Martinez


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
            raise Exception("PROGRAM QUIT VOLUNTARILY")
        
        # These keys are purely for debug. TODO: REMEMBER TO DELETE THEM LATER
        if pressed_keys[pygame.K_1]:
            if self.runonce == 0:
                self.game.emptyanimation = True
                self.game.gamestate = 1
            self.runonce = 1
        
        if pressed_keys[pygame.K_2]:
            if self.runonce == 0:
                self.game.debugspawnbreakout()
                self.game.gamestate = 2
            self.runonce = 1

        if pressed_keys[pygame.K_RSHIFT]:
            self.runonce = 0

        if pressed_keys[pygame.K_LSHIFT]:
            if self.runonce == 0:
                self.game.tetrisgrid.checkrow()
            self.runonce = 1


        # ACTUAL KEYS

        if self.key_was_pressed_on_this_cycle(pygame.K_s, events) or self.key_was_pressed_on_this_cycle(pygame.K_DOWN, events):
            self.game.speedchange = True
            self.game.newspeed = 1
        
        if self.key_was_released_on_this_cycle(pygame.K_s, events) or self.key_was_released_on_this_cycle(pygame.K_DOWN, events):
            self.game.speedchange = True
            self.game.newspeed = self.game.levelspeed

        if self.key_was_pressed_on_this_cycle(pygame.K_a, events) or self.key_was_pressed_on_this_cycle(pygame.K_LEFT, events):
            self.game.tetrominomovedir = -8
            self.game.tetrominomoving = True    
        
        if self.key_was_pressed_on_this_cycle(pygame.K_d, events) or self.key_was_pressed_on_this_cycle(pygame.K_RIGHT, events):
            self.game.tetrominomovedir = 8
            self.game.tetrominomoving = True

        if self.key_was_pressed_on_this_cycle(pygame.K_w, events) or self.key_was_pressed_on_this_cycle(pygame.K_UP, events):
            self.game.tetrominorotating = True

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

    @staticmethod
    def key_was_released_on_this_cycle(key, events):
        for event in events:
            if event.type == pygame.KEYUP and event.key == key:
                return True
        return False
