import pygame
from tetrisgrid import tetrisgrid
from filesystem import file

class Block():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.health = 1
        self.is_dead = False

class Wall():
    def __init__(self, screen): #Trying to get the Tetris blocks onto the breakout game
        self.screen = screen
        self.blocks = []
        for j in range(len(tetrisgrid.get_filled())):
            for k in range(8):
                self.blocks.append(tetrisgrid.get_filled())

class Ball():
    def __init__(self, screen, start_x, start_y, speed_x, speed_y):
        self.screen = screen
        self.x = start_x
        self.y = start_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = 4
        self.color = (255, 255, 255)
        self.score = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        # Parameters (screen, color, start position, radius)

    def move(self):
        self.y += self.speed_y
        self.x += self.speed_x
        if self.y + self.radius > 184 or self.y - self.radius < 0:
            self.speed_y = - self.speed_y
        if self.x - self.radius < 0:
            self.speed_x = - self.speed_x
        if self.x + self.radius > 244:
            raise Exception("GAME OVER")

    # def give_x(self):
    #     return self.x
    #
    # def give_y(self):
    #     return self.y

    def bonk_top(self):
        self.speed_x = -self.speed_x
        self.speed_y = abs(self.speed_y)
        self.score += 5 + self.score ** 4

    def bonk_bottom(self):
        self.speed_x = -self.speed_x
        self.speed_y = -abs(self.speed_y)
        self.score += 5 + self.score ** 4

    # def bomb(self):
    #     if power_bomb == True:
    #         self.color = (150, 100, 80)
    def update_score(self):
        return self.score


class Paddle:
    def __init__(self, screen, y):
        self.x = 224
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(file("test_paddle.png"))
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        # self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.top_hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.bottom_hitbox = pygame.Rect(self.x, self.y - self.image.get_height(), self.image.get_width(), self.image.get_height())

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.image, (self.x, self.y - self.image.get_height()))
        # pygame.draw.line(screen, (255, 255, 255), (self.x, self.y + .5 * self.height), (self.x, self.y - .5 * self.height), 4)
        # Parameters (screen, color, start position, radius)

    def give_top(self):
        return self.top_hitbox

    def give_bottom(self):
        return self.bottom_hitbox


    # def expand_paddle(self):
    #     if power_long == True:
    #         self.height = self.height * 2

