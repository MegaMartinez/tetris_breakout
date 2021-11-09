import pygame
from tetrisgrid import tetrisgrid
from tile import tile
from Tetromino import Tetromino

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
        self.tetronimo = Tetromino("I")
        self.speed = 15

        # Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)
        #     self.enemies = Enemies(self.screen)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        for k in range(len(self.tetrisgrid.row)):
            for k2 in range(len(self.tetrisgrid.row[k])):
                self.tetrisgrid.row[k][k2].draw(self.screen)
        if self.tetronimo != None:
            self.tetronimo.draw(self.screen)


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
            self.framecount += 1
        

        if self.tetrisinaction:
            self.tetrisgrid.updatestops()
            if self.framecount == self.speed:
                self.tetronimo.movedown()
                self.framecount = 0
            for k in range(len(self.tetronimo.positions)):
                if self.tetronimo.positions[k] in self.tetrisgrid.get_stopspots():
                    for k2 in range(len(self.tetronimo.positions)):
                        self.tetrisgrid.fill((self.tetronimo.positions[k2][0] // 8) - 8, (self.tetronimo.positions[k2][1] // 8) - 3, self.tetronimo.color)
                    self.tetrisinaction = False
                    self.tetronimo = None
                    break
            self.framecount += 1

        

            
        #     self.enemies.move()
        #     self.missiles.handle_explosions(self.enemies)
