import pygame


class Ball():
    def __init__(self, screen, start_x, start_y, speed_x, speed_y):
        self.screen = screen
        self.x = start_x
        self.y = start_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = 4

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
        # Parameters (screen, color, start position, radius)

    def move(self):
        self.y += self.speed_y
        self.x += self.speed_x
        if self.y + self.radius > 184 or self.y - self.radius < 0:
            self.speed_y = - self.speed_y
        if self.x + self.radius > 244 or self.x - self.radius < 0:
            self.speed_x = - self.speed_x

    # def give_x(self):
    #     return self.x
    #
    # def give_y(self):
    #     return self.y

    def bonk_top(self):
        self.speed_x = -self.speed_x
        self.speed_y = -self.speed_y

    def bonk_bottom(self):
        self.speed_x = -self.speed_x
        self.speed_y = -self.speed_y


class Paddle:
    def __init__(self, screen, x, y, height, width):
        self.x = x
        self.y = y
        self.screen = screen
        self.height = height
        self.width = width
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y + .5*self.height), (self.x, self.y - .5*self.height), 4)
        # Parameters (screen, color, start position, radius)

