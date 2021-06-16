import pygame
from objects import Objects

class Car(Objects):
    def __init__(self, startpos, wh=True, texture_path = "C:/Users/georg/PycharmProjects/Neuro race/venv/textures/game_car.png"):
        super().__init__()
        if wh:
            self.texture = pygame.image.load(texture_path)
            self.rect = self.texture.get_rect()
        else:
            self.texture = pygame.transform.scale(pygame.image.load(texture_path), wh)
            self.rect = self.texture.get_rect()

        self.rect.center = (startpos[0], startpos[1])
        self.degree = 0
        self.x, self.y = self.rect.center[0], self.rect.center[1]

    def rotate(self, deg):
        self.texture = pygame.transform.rotate(self.texture, deg)
        self.rect = self.texture.get_rect()
        self.rect.center = (self.x, self.y)

    def move(self, to):
        self.rect = self.rect.move(to)
        self.x, self.y = self.rect.center[0], self.rect.center[1]