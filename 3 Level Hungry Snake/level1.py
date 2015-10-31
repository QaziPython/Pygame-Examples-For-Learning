#!/Users/Rafeh/anaconda/envs/python2/bin python
############################################################################
# Purpose : A very small, basic and my first game
# Usages : Learning purpose
# Start date : 10/31/2015
# End date : In progress
# Author : Ankur Aggarwal
# Editor : Rafeh Qazi
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Version : 0.0.2
# Modification history : level1-Snake passage through the border
############################################################################


import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()
COUNTER=0

def main():
    COUNTER = 0
    STATE = []
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4
    STEP = 20
    BLOCK = [20, 20]

    # random coordinates x, y used for initializing snake
    X = randint(1, 20)
    Y = randint(2, 22)
    SNAKE = [int(X*20), int(Y*20)]
    SNAKELIST = [[X*20, Y*20], [(X-20)*20, (Y*20)]]

    # initialize random apple coordinate
    APPLE = (int(randint(1, 31)*STEP), int(randint(2, 22)*STEP))

    DEAD = 0
    DIRECTION = RIGHT
    SCORE = 0
    FONT1 = pygame.font.SysFont("Arial", 30)
    SCREEN = pygame.display.set_mode((640, 480), 0, 24)
    CLOCK = pygame.time.Clock()

    # blast function used for creating the blast through sprites on collision
    def blast(w, h):
        image = pygame.image.load("explosed-sprite.png").convert_alpha()
        width, height = image.get_size()
        for i in xrange(int(width/w)):
            STATE.append(image.subsurface((i*w, 0, w, h)))

    # game loop
    while not DEAD:
        pressed = pygame.key.get_pressed()
        # pygame.event.get() returns a dict of current state of the game
        for event in pygame.event.get():
            if event.type == QUIT or pressed[K_q]:
                exit()
        if pressed[K_h] and DIRECTION != RIGHT:
            DIRECTION = LEFT
        elif pressed[K_l] and DIRECTION != LEFT:
            DIRECTION = RIGHT
        elif pressed[K_k] and DIRECTION != DOWN:
            DIRECTION = UP
        elif pressed[K_j] and DIRECTION != UP:
            DIRECTION = DOWN
        if DIRECTION == RIGHT:
            SNAKE[0] = SNAKE[0]+STEP
            if SNAKE[0] >= 640:
                SNAKE[0] = 0

        elif DIRECTION == LEFT:
            SNAKE[0] = SNAKE[0]-STEP
            if SNAKE[0] < 0:
                SNAKE[0] = 620

        elif DIRECTION == UP:
            SNAKE[1] = SNAKE[1]-STEP
            if SNAKE[1] < 0:
                SNAKE[1] = 460
        elif DIRECTION == DOWN:
            SNAKE[1] = SNAKE[1]+STEP
            if SNAKE[1] >= 480:
                SNAKE[1] = 0

        if SNAKELIST.count(SNAKE) > 0:
            DEAD = 1

        SNAKELIST.insert(0, list(SNAKE))
        if SNAKE[0] == APPLE[0] and SNAKE[1] == APPLE[1]:
            APPLE = (int(randint(1, 31)*STEP), int(randint(2, 22)*STEP))
            SCORE = SCORE+1
        else:
            SNAKELIST.pop()
        # display on the screen
        SCREEN.fill((0, 0, 0))
        scr = pygame.font.SysFont("Arial", 20)
        display_score = scr.render("Score : %d" % SCORE, True, (0, 255, 0))
        SCREEN.blit(display_score, (500, 10))
        FONT1 = pygame.font.SysFont("Arial", 30)
        SCREEN.blit(FONT1.render("phajanngggg", True, (0, 255, 0)), (50, 250))
        pygame.draw.rect(SCREEN, (255, 0, 0), Rect(APPLE, BLOCK), 0)
        for i in SNAKELIST:
            pygame.draw.rect(SCREEN, (0, 255, 0), Rect(i, BLOCK))
        pygame.display.flip()
        CLOCK.tick(15)

    if DEAD == 1:
        blast(20, 20)
        for _ in xrange(7):
            SCREEN.blit(STATE[COUNTER], (SNAKE[0], SNAKE[1]))
            COUNTER = (COUNTER+1) % 7
            pygame.display.update()
            CLOCK.tick(10)
        # game over
        SCREEN.fill((0, 0, 0))
        over = pygame.font.SysFont("Arial", 40)
        display_game_over = over.render("GAME OVER", True, (0, 255, 0))
        SCREEN.blit(display_game_over, (50, 50))
        SCREEN.blit(display_score, (200, 200))
        SCREEN.blit(FONT1.render("Press P To Play Again", True,
                                 (0, 255, 0)), (50, 250))
        SCREEN.blit(FONT1.render("Press Q to Quit", True,
                                 (0, 255, 0)), (50, 350))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            pressed = pygame.key.get_pressed()
            # quit on Q
            if pressed[K_q]:
                exit()
            if pressed[K_p]:
                main()


if __name__ == '__main__':
    main()
