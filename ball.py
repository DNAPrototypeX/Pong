import pygame
import random


class Ball:
    def __init__(self, screen, rect, colour, players):
        self.rect = pygame.Rect(rect)
        self.screen = screen
        self.colour = colour
        self.players = players
        self.x_speed = -4
        self.y_speed = 0
        self.player1_score = 0
        self.player2_score = 0
        self.total_rebounds = 0

    def update(self):

        if self.rect.y < 0:
            self.y_speed *= -1
        elif self.rect.y > 480:
            self.y_speed *= -1

        if self.rect.x > 680:
            self.rect.x = 330
            self.rect.y = 230
            self.y_speed = 0
            self.x_speed = 4
            self.player1_score += 1
            self.total_rebounds = 0

        elif self.rect.x < 0:
            self.rect.x = 330
            self.rect.y = 230
            self.y_speed = 0
            self.x_speed = -4
            self.player2_score += 1
            self.total_rebounds = 0

        for player in self.players:
            if self.rect.colliderect(player):
                self.total_rebounds += 1
                if player == self.players[0]:
                    if player.rect.colliderect(self.rect.x - self.x_speed, self.rect.y
                                               , self.rect.width, self.rect.height):
                        self.y_speed *= -1
                    else:
                        self.x_speed *= -1
                        self.x_speed += self.total_rebounds * 0.05
                elif player == self.players[1]:
                    if player.rect.colliderect(self.rect.x - self.x_speed, self.rect.y
                                               , self.rect.width, self.rect.height):
                        self.y_speed *= -1
                    else:
                        self.x_speed *= -1
                        self.x_speed -= self.total_rebounds * 0.05
                if player.speed != 0:
                    if player.speed > 0:
                        self.y_speed -= 1 + (random.random() * 1.5)
                    elif player.speed < 0:
                        self.y_speed += 1 + (random.random() * 1.5)

        self.rect.move_ip(self.x_speed, self.y_speed)
        pygame.draw.rect(self.screen, self.colour, self.rect)
