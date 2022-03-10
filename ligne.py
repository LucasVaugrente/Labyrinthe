import pygame


class Ligne(pygame.sprite.Sprite):

    def __init__ (self, x, y):
        x = x * 10
        y = y * 10
        super().__init__()

