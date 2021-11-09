import pygame
from tetrisgrid import tetrisgrid
from tile import tile
from Tetromino import Tetromino
import random

# Put each class in its own module, using the same name for both.
# Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter
#     from Missiles import Missiles
#     from Enemies import Enemies

# TODO: Put your names here (entire team)


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.tetrisgrid = tetrisgrid()
        self.framecount = 0
        self.emptyanimation = False
        self.tetrisinaction = False
        self.tetromino = None
        self.stoptetromino = False
        self.clearanim = False
        self.tetrominomoving = False
        self.speedchange = False
        self.tetrominomovedir = 0
        self.speed = 15
        self.newspeed = 0
        self.tetrisstage = 0
        self.levelspeed = 15

        # Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)
        #     self.enemies = Enemies(self.screen)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        for k in range(len(self.tetrisgrid.row)):
            for k2 in range(len(self.tetrisgrid.row[k])):
                self.tetrisgrid.row[k][k2].draw(self.screen)
        if self.tetromino != None:
            self.tetromino.draw(self.screen)


        # Use something like the following, but for the objects in YOUR game:
        #     self.fighter.draw()
        #     self.missiles.draw()
        #     self.enemies.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # Use something like the following, but for the objects in YOUR game:
        if self.emptyanimation:
            if self.framecount in [8, 16, 24, 32]:
                self.tetrisgrid.clear_next_frame()
            if self.framecount == 32:
                self.emptyanimation = False
                self.framecount = -1
                self.tetrisstage = 1
            self.framecount += 1
        

        if self.tetrisinaction:
            self.tetrisgrid.updatestops()
            if self.framecount == self.speed:
                self.tetromino.movedown()
                self.framecount = 0
            for k in range(len(self.tetromino.positions)):
                if self.tetromino.positions[k] in self.tetrisgrid.get_stopspots():
                    self.stoptetromino = True
                    self.tetrisinaction = False
                    self.framecount = -1
                    break
            self.framecount += 1

        if self.stoptetromino:
            if self.framecount == self.speed * 2:
                for k in range(len(self.tetromino.positions)):
                    if self.tetromino.positions[k] in self.tetrisgrid.get_stopspots():
                        for k2 in range(len(self.tetromino.positions)):
                            self.tetrisgrid.fill((self.tetromino.positions[k2][0] // 8) - 8, (self.tetromino.positions[k2][1] // 8) - 3, self.tetromino.color)
                        self.tetromino = None
                        self.framecount = -1
                        self.stoptetromino = False
                        self.tetrisinaction = False
                        self.tetrisgrid.checkrow()
                        self.spawntetromino()
                        break
                    else:
                        self.stoptetromino = False
                        self.tetrisinaction = True
                        self.framecount = 0
            self.framecount += 1
        
        if self.tetrisgrid.row[0][4].state == 2:
            raise Exception("GAME OVER")

        if self.tetrominomoving:
            if self.tetromino != None:
                self.tetromino.movehorizontal(self.tetrominomovedir, self.tetrisgrid.get_filled())
            self.tetrominomoving = False

        if self.speedchange:
            self.speed = self.newspeed
            self.speedchange = False
            self.framecount = 0
            

        #     self.enemies.move()
        #     self.missiles.handle_explosions(self.enemies)

    def spawntetromino(self):
        i = random.randrange(0, 7, 1)
        self.tetromino = Tetromino(["I", "J", "L", "O", "T", "S", "Z"][i])
        self.tetrisinaction = True