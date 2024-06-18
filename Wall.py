import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()
        self.image.fill("#715fde")
        self.rect.x=x
        self.rect.y=y