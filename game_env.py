import pygame
import math
import sys
import os
import random
from field import Field
from cars import Car
class Main():
    def __init__(self, width, height, FPS):
        field = Field(width, height)
        pygame.init()
        self.screen = pygame.display.set_mode((field.width, field.height))
        pygame.display.set_caption("Neural race")
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.car = Car((field.width // 2, field.height // 2))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.car.move((0, -1))
            elif keys[pygame.K_s]:
                self.car.move((0, +1))

            if keys[pygame.K_d]:
                self.car.move((1, 0))
                self.car.rotate(1)
            elif keys[pygame.K_a]:
                self.car.move((-1, 0))
                self.car.rotate(-1)

            self.render()
            self.clock.tick(self.FPS)

    def render(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.car.texture, self.car.rect)
        pygame.display.flip()