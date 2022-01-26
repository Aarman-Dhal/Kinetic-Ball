import random
import pygame
import time

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kinetic Ball")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

class Ball():
    def __init__(self, color):
        self.x_pos= []
        self.y_pos = []
        self.dx_vals = [-0.05, 0.015, -0.01, 0.01, 0.005, -0.005]
        self.dx_pos = []
        self.dy_pos = []
        self.gravity = 0.0001
        self.color = color
        self.width = 30

    def find_position(self):
        position = pygame.mouse.get_pos()
        self.x_pos.append(position[0])
        self.y_pos.append(position[1])
        self.dx_pos.append(random.choice(self.dx_vals))
        self.dy_pos.append(0)
    
    def update(self):
        for i in range(len(self.x_pos)):
            self.x_pos[i] += self.dx_pos[i]
            self.y_pos[i] += self.dy_pos[i]
            self.dy_pos[i] += self.gravity

            if self.x_pos[i] - self.width< 0:
                self.dx_pos[i] *= -1
            elif self.x_pos[i] + self.width > screen_width:
                self.dx_pos[i] *= -1
            if self.y_pos[i] > 360:
                self.dy_pos[i] *= -1
    
    def draw(self):
        self.start_time = time.time()
        for i in range(len(self.x_pos)):
            pygame.draw.circle(screen, self.color, (self.x_pos[i], self.y_pos[i]), self.width)
    
class Elastic(Ball):
    def __init__(self, color):
        super().__init__(color)
        self.gravity = 0.0001
    
class Inelastic(Ball):
    def __init__(self, color):
        super().__init__(color)
        self.gravity = 0.0001

    def drag(self):
        for i in range(len(self.x_pos)):
            self.dy_pos[i] *= 0.9999

elastic_ball = Elastic(white)
inelastic_ball = Inelastic(red)


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                elastic_ball.find_position()
            elif event.button == 3:
                inelastic_ball.find_position()

    elastic_ball.update()
    inelastic_ball.update()
    inelastic_ball.drag()

    screen.fill(black)
    pygame.draw.line(screen, white, (0, 400), (screen_width, 400), 20)
    
    elastic_ball.draw()
    inelastic_ball.draw()

    pygame.display.flip()

pygame.quit()