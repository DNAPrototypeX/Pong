import pygame
pygame.init()

class Player:
    def __init__(self, screen, rect, colour):
        self.rect = pygame.Rect(rect)
        self.colour = colour
        self.screen = screen
        self.speed = 0

    def update(self):
        if self.rect.y < 0:
            self.speed = 0
            self.rect.y = 0
        elif self.rect.y > 400:
            self.speed = 0
            self.rect.y = 400
        self.rect.y += self.speed
        pygame.draw.rect(self.screen, self.colour, self.rect)
