import pygame
from tetrisgrid import tetrisgrid
# from tile import tile
from Tetromino import Tetromino
from Scoreboard import Scoreboard
import random
import Ball
from Powerup import powerup
from filesystem import file

# Put each class in its own module, using the same name for both.
# Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter
#     from Missiles import Missiles
#     from Enemies import Enemies

# Maddie Fletcher, Luca Acquasaliente, Matthew Martinez


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.tetrisgrid = tetrisgrid()
        self.framecount = 0
        self.framecountY = 0
        self.framecountO = 0
        self.framecountG = 0
        self.framecountP = 0
        self.round = 0



        """
        game states
        0 = menu
        1 = tetris
        2 = breakout
        """

        self.gamestate = 0

        # ------------------ #
        # TETRIS VARIABLES   #
        # ------------------ #
        self.screen = screen
        self.emptyanimation = False
        self.tetrisinaction = False
        self.tetromino = None
        self.stoptetromino = False
        self.clearanim = False
        self.tetrominomoving = False
        self.speedchange = False
        self.tetrominorotating = False
        self.tetrominomovedir = 0
        self.speed = 15
        self.newspeed = 0
        self.tetrisstage = 0
        self.levelspeed = 15
        self.lastpickedshape = None
        self.moveback = False
        self.nextround = False



        self.ball = None
        self.paddle = None
        self.movegrid = False
        self.powerup = None
        self.paddle_speed = 3


        self.scoreboard = Scoreboard(self.screen)
        self.score = 0

        self.activepowerups = []

        # Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)
        #     self.enemies = Enemies(self.screen)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        for k in range(len(self.tetrisgrid.row)):
            for k2 in range(len(self.tetrisgrid.row[k])):
                # self.scoreboard.draw()
                self.tetrisgrid.row[k][k2].draw(self.screen)
        if self.tetromino != None:
            self.tetromino.draw(self.screen)

        if self.ball != None:
            self.ball.draw(self.screen)
            self.paddle.draw()
        
        if self.powerup != None:
            self.powerup.draw(self.screen)
        
        self.screen.blit(pygame.image.load(file("placeholderblack.png")), (0, 0))

        self.scoreboard.draw()



        # Use something like the following, but for the objects in YOUR game:
        #     self.fighter.draw()
        #     self.missiles.draw()
        #     self.enemies.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # Use something like the following, but for the objects in YOUR game:

        if self.gamestate == 1:

            if True not in [self.emptyanimation, self.tetrisinaction, self.stoptetromino, self.moveback] or self.nextround:
                pygame.time.wait(1000)
                self.spawntetromino()
                self.nextround = False

            if self.moveback:       # Moves the tetris grid for tetris after breakout
                if self.framecount % 4 == 0:
                    self.tetrisgrid.moveeverythingback()
                if self.framecount == 128:
                    self.moveback = False
                    self.framecount = -1
                    self.nextround = True
                self.framecount += 1
            else:
                if self.emptyanimation:
                    if self.framecount in [8, 16, 24, 32]:
                        self.tetrisgrid.clear_next_frame()
                    if self.framecount == 32:
                        self.emptyanimation = False
                        self.framecount = -1
                    self.framecount += 1

                if self.tetrominorotating:
                    self.tetromino.rotate(self.tetrisgrid.get_filled())
                    self.tetrominorotating = False

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
                                ran = random.randrange(1, 3)
                                drop = pygame.mixer.Sound(file("soundeffects/drop_" + str(ran) + ".wav"))
                                pygame.mixer.Sound.play(drop)
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
                    self.gamestate = 2
                    self.tetromino = None
                    self.framecount = 0
                    self.movegrid = True
                    # raise Exception("GAME OVER")

                if self.tetrominomoving:
                    if self.tetromino != None:
                        self.tetromino.movehorizontal(self.tetrominomovedir, self.tetrisgrid.get_filled())
                    self.tetrominomoving = False

                if self.speedchange and not self.emptyanimation:
                    self.speed = self.newspeed
                    self.speedchange = False
                    self.framecount = 0

                self.score += self.tetrisgrid.update_score()
                self.scoreboard.score = self.score

        # Starting Breakout 22222222222222222222222222222222222222222222222222
        if self.gamestate == 2:     # starts the breakout game
            if self.movegrid:       # Moves the tetris grid for breakout
                if self.framecount % 4 == 0:
                    self.tetrisgrid.moveeverything()
                if self.framecount == 128:
                    self.movegrid = False
                    self.framecount = -1
                    self.debugspawnbreakout()
                self.framecount += 1
            else:       # begins ball movement
                self.tetrisgrid.updatehitbox()
                self.ball.move()
                if self.powerup != None:        # moves the powerup
                    self.powerup.move()
                    if self.powerup.x < 0:
                        self.powerup = None

                if self.paddle.give_top().collidepoint(self.ball.x, self.ball.y):       # collides top paddle
                    self.ball.bonk_top()

                if self.paddle.give_bottom().collidepoint(self.ball.x, self.ball.y):    # collides bottom paddle
                    self.ball.bonk_bottom()

                if self.powerup != None:        # detects collision between powerup and paddle
                    if self.paddle.give_top().collidepoint(self.powerup.x, self.powerup.y) or self.paddle.give_bottom().collidepoint(self.powerup.x, self.powerup.y):
                        self.powerup.activate(self)
                        self.powerup = None
                    
                    # if self.paddle.give_bottom().collidepoint(self.powerup.x, self.powerup.y):
                    #     self.powerup.activate(self)
                    #     self.powerup = None






                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:       # moves paddle
                    if self.paddle.y > self.paddle.height + self.paddle.height:
                        self.paddle.y -= self.paddle_speed
                        self.paddle.top_hitbox.y -= self.paddle_speed
                        self.paddle.bottom_hitbox.y -= self.paddle_speed

                if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
                    if self.paddle.y < self.screen.get_height() - self.paddle.height:
                        self.paddle.y += self.paddle_speed
                        self.paddle.top_hitbox.y += self.paddle_speed
                        self.paddle.bottom_hitbox.y += self.paddle_speed

                self.tetrisgrid.checkhit(self.ball.x, self.ball.y, self.ball, self)

                if "yellow" in self.activepowerups:
                    if self.framecountY == 600:
                        self.paddle.short_paddle()
                        self.framecountY = -1
                        self.activepowerups.remove("yellow")
                    self.framecountY += 1

                if "green" in self.activepowerups:
                    if self.framecountG == 600:
                        self.ball.change_score_decr()
                        self.framecountG = -1
                        self.activepowerups.remove("green")
                    self.framecountG += 1

                if "orange" in self.activepowerups:
                    if self.framecountO == 420:
                        self.change_paddle_speed(2)
                        self.framecountO = -1
                        self.activepowerups.remove("orange")
                    self.framecountO += 1

                if "purple" in self.activepowerups:
                    if self.framecountO == 900:
                        self.ball.change_speed(False)
                        self.framecountO = -1
                        self.activepowerups.remove("purple")
                    self.framecountO += 1


                self.score += self.ball.update_score()
                self.scoreboard.score = self.score

                if self.tetrisgrid.get_filled() == []:
                    self.paddle_speed = 3
                    self.ball = None
                    self.paddle = None
                    self.powerup = None
                    self.activepowerups = []
                    self.moveback = True
                    self.gamestate = 1
        #     self.enemies.move()
        #     self.missiles.handle_explosions(self.enemies)

    def spawntetromino(self):
        letterlist = ["I", "J", "L", "O", "T", "S", "Z"]
        if self.lastpickedshape != None:
            letterlist.remove(self.lastpickedshape)
        self.lastpickedshape = random.choice(letterlist)
        self.tetromino = Tetromino(self.lastpickedshape)
        self.tetrisinaction = True
    
    def debugspawnbreakout(self):
        self.ball = Ball.Ball(self.screen, 16, 50, 1, .5)
        # self.paddle_top = Ball.Paddle(self.screen, 192, 72, 32, 4)
        # self.paddle_bottom = Ball.Paddle(self.screen, 192, 96, 32, 4)
        self.paddle = Ball.Paddle(self.screen, 92)

    def change_paddle_speed(self, newspeed):    # change paddle speed for powerup
        self.paddle_speed = newspeed

    def spawnpowerup(self, color, x, y):    # spawns powerup
        self.powerup = powerup(color, x, y)

    def blowup(self):
        self.tetrisgrid.blowup(self.ball)
        self.activepowerups.remove("blue")

    def debugwinbreakout(self):
        for ky in range(20):
            for kx in range(10):
                self.tetrisgrid.row[ky][kx].empty_basic()