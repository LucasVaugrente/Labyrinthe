import pygame

class Joueur(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()
        self.image.fill((255, 255, 0))
