import random

import pygame
# from tetrisgrid import tetrisgrid
from filesystem import file
# Code by Maddie Fletcher


class Ball:
    def __init__(self, screen, start_x, start_y, speed_x, speed_y):
        self.screen = screen
        self.x = start_x
        self.y = start_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = 3
        self.color = (255, 255, 255)
        self.score = 0
        self.score_incr = 10
        self.k = 1

    def draw(self, screen):     # Draws the ball on the screen
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        # Parameters (screen, color, start position, radius)

    def move(self):     # Moves the ball, loses if the ball passes paddle, bounces of the sides.
        self.y += self.speed_y
        self.x += self.speed_x
        if self.y + self.radius > 184 or self.y - self.radius < 23:
            self.speed_y = - self.speed_y
        if self.x + self.radius > 180:
            self.speed_x = - self.speed_x
        if self.x - self.radius < 6:
            raise Exception("GAME OVER")

    # def give_x(self):
    #     return self.x
    #
    # def give_y(self):
    #     return self.y

    def bonk_top(self):     # reflecting ball off the top of the paddle
        playsound()
        ran = random.uniform(-0.2, 0.2)
        self.speed_x = -self.speed_x
        if abs(self.speed_y) < .5:
            ran = .2
            self.speed_y = abs(self.speed_y) + ran
        elif abs(self.speed_y) > 1.5:
            ran = -.2
            self.speed_y = abs(self.speed_y) + ran
        else:
            self.speed_y = abs(self.speed_y) + ran

    def bonk_bottom(self):      # reflecting ball of bottom of the paddle
        playsound()
        ran = random.uniform(-0.2, 0.2)
        self.speed_x = -self.speed_x
        if abs(self.speed_y) < .5:
            ran = .2
            self.speed_y = -abs(self.speed_y) + ran
        elif abs(self.speed_y) > 1.5:
            ran = -.2
            self.speed_y = -abs(self.speed_y) + ran
        else:
            self.speed_y = -abs(self.speed_y) + ran

    def bonk_block_side(self):      # reflecting off the side of a block
        playsound()
        self.speed_x = -self.speed_x
        self.score += self.score_incr

    def bonk_block_top(self):       # reflecting off the top or bottom of a block
        playsound()
        self.speed_y = -self.speed_y
        self.score += self.score_incr

    def change_speed(self, inc):    # changes speed for the slow ball powerup
        if inc:
            self.speed_y = self.speed_y * 0.5
            self.speed_x = self.speed_x * 0.5
        else:
            self.speed_y = self.speed_y * 2
            self.speed_x = self.speed_x * 2

    def change_score_incr(self):     # increases score for powerup
        self.score_incr = self.score_incr * 2

    def change_score_decr(self):
        self.score_incr = self.score_incr // 2

    def update_score(self):
        x = self.score
        self.score = 0
        return x


class Paddle:
    def __init__(self, screen, y):
        self.x = 4
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(file("test_paddle.png"))
        self.image2 = pygame.image.load(file("test_paddle2.png"))
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.top_hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.bottom_hitbox = pygame.Rect(self.x, self.y - self.image.get_height(), self.image.get_width(), self.image.get_height())

    def draw(self):     # draws the paddle in 2 halves for hitbox detection
        self.screen.blit(self.image2, (self.x, self.y))
        self.screen.blit(self.image, (self.x, self.y - self.image.get_height()))

    def give_top(self):
        return self.top_hitbox

    def give_bottom(self):
        return self.bottom_hitbox

    def long_paddle(self):      # makes long paddle and updates hitbox for long paddle powerup
        self.image = pygame.image.load(file("test_paddle_long.png"))
        self.image2 = pygame.image.load(file("test_paddle_long2.png"))
        self.top_hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.bottom_hitbox = pygame.Rect(self.x, self.y - self.image.get_height(), self.image.get_width(), self.image.get_height())

    def short_paddle(self):     # returns the paddle to being small for paddle powerup
        self.image = pygame.image.load(file("test_paddle.png"))
        self.image2 = pygame.image.load(file("test_paddle2.png"))
        self.top_hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.bottom_hitbox = pygame.Rect(self.x, self.y - self.image.get_height(), self.image.get_width(), self.image.get_height())



def playsound():
    ran = random.randrange(1, 4)
    beep = None
    if ran == 1:
        beep = pygame.mixer.Sound(file("soundeffects/beep_square_50_1.wav"))
    elif ran == 2:
        beep = pygame.mixer.Sound(file("soundeffects/beep_square_50_2.wav"))
    elif ran == 3:
        beep = pygame.mixer.Sound(file("soundeffects/beep_square_50_3.wav"))
    else:
        raise Exception("the sound effects are not working")
    pygame.mixer.Sound.play(beep)
