import pygame
import random
import sys


class Ball:
    def __init__(self, screen, rect, colour, players):
        self.rect = pygame.Rect(rect)
        self.screen = screen
        self.colour = colour
        self.players = players
        self.x_speed = -4
        self.y_speed = 0

    def update(self):

        if self.rect.y < 0:
            self.y_speed *= -1
        elif self.rect.y > 480:
            self.y_speed *= -1

        for player in self.players:
            if self.rect.colliderect(player):
                self.x_speed *= -1

                if player.speed != 0:
                    if player.speed > 0:
                        self.y_speed = (self.y_speed * -1) - random.randrange(1, 2)
                    elif player.speed < 0:
                        self.y_speed = (self.y_speed * -1) + random.randrange(1, 2)

        self.rect.move_ip(self.x_speed, self.y_speed)
        pygame.draw.rect(self.screen, self.colour, self.rect)
