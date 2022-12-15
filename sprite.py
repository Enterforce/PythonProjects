import pygame
import game

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startX, startY):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startX, startY]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
