    # Paul Moore

def Main():
    import pygame
    from player import Player
    from ball import Ball
    import sys

    # Define some colors, you may want to add more
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Setup

    players = [Player(screen, (30, 200, 20, 100), WHITE),
               Player(screen, (650, 200, 20, 100), WHITE)]
    ball = Ball(screen, (330, 230, 20, 20), WHITE, players)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    title_screen = pygame.image.load('titlescreen.png').convert()
    pygame.mixer.music.load('music.wav')
    muted = pygame.image.load('music_muted.png')
    unmuted = pygame.image.load('music_playing.png')
    mute_rect = pygame.Rect(300, 10, 50, 40)


    def waitforkeypress():
        music_ismuted = False
        while True:
            mpos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    return music_ismuted
                if event.type == pygame.MOUSEBUTTONDOWN and mute_rect.collidepoint(mpos[0], mpos[1]):
                    if music_ismuted:
                        music_ismuted = False
                    else:
                        music_ismuted = True
            screen.blit(title_screen, (0, 0))
            if music_ismuted:
                screen.blit(muted, (300, 10))
                pygame.mixer.music.pause()
            else:
                screen.blit(unmuted, (300, 10))
                pygame.mixer.music.unpause()

            pygame.display.flip()

    def gameover():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_y:
                        Main()
                    elif event.key == pygame.K_n:
                        return
    pygame.mixer.music.play(-1)
    music_ismuted = waitforkeypress()
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        mpos = pygame.mouse.get_pos()
        # --- All events are detected here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    players[0].speed = -4
                elif event.key == pygame.K_s:
                    players[0].speed = 4
                elif event.key == pygame.K_UP:
                    players[1].speed = -4
                elif event.key == pygame.K_DOWN:
                    players[1].speed = 4
                elif event.key == pygame.K_x:
                    ball.x_speed *= 1.25
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    players[0].speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    players[1].speed = 0
            if event.type == pygame.MOUSEBUTTONDOWN and mute_rect.collidepoint(mpos[0], mpos[1]):
                if music_ismuted:
                    music_ismuted = False
                else:
                    music_ismuted = True
        # --- Game logic should go here

        # --- Screen-clearing code goes here
        #  Here, we clear the screen to white.
        screen.fill(BLACK)

        # --- Drawing code should go here
        ball.update()
        if ball.player1_score == 5 or ball.player2_score == 11:
            done = True
        for player in players:
            player.update()
        p1_score = font.render(str(ball.player1_score), True, WHITE)
        p2_score = font.render(str(ball.player2_score), True, WHITE)
        screen.blit(p1_score, (10, 10))
        screen.blit(p2_score, (670, 10))
        if music_ismuted:
            screen.blit(muted, (300, 10))
            pygame.mixer.music.pause()
        else:
            screen.blit(unmuted, (300, 10))
            pygame.mixer.music.unpause()
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


    # Close the window and quit.
    sys.exit()
Main()