import pygame

class Mur(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()
        self.image.fill((0,0,255))
        self.rect.x=x
        self.rect.y=y