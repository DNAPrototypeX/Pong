import pygame
import random
pygame.init()
collide_player = pygame.mixer.Sound('player_collide.wav')
collide_wall = pygame.mixer.Sound('wall_collide.wav')
point_scored = pygame.mixer.Sound('point_scored.wav')

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
            collide_wall.play()
            self.y_speed *= -1
        elif self.rect.y > 480:
            collide_wall.play()
            self.y_speed *= -1

        if self.rect.x > 680:
            point_scored.play()
            self.rect.x = 330
            self.rect.y = 230
            self.y_speed = 0
            self.x_speed = 4
            self.player1_score += 1
            self.total_rebounds = 0

        elif self.rect.x < 0:
            point_scored.play()
            self.rect.x = 330
            self.rect.y = 230
            self.y_speed = 0
            self.x_speed = -4
            self.player2_score += 1
            self.total_rebounds = 0

        for player in self.players:
            if self.rect.colliderect(player):
                collide_player.play()
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
