from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import math
import sys
import random
from decimal import *



def main():

    # some config
    FPS = 120
    PPS = 100 # points per seconds
    
    COLOR1 = (0, 238, 255)
    COLOR2 = (255, 153, 0)


    # window config
    pygame.init()
    pygame.display.set_caption('Pi Calculation')
    screen_width, screen_height = 400, 400
    screen = pygame.display.set_mode((screen_width, screen_height))

    # configure circle
    circle_pos = (screen_width//2, screen_height//2)
    circle_radius =  min(circle_pos)

    # precision setting
    sys.maxsize = 50
    getcontext().prec = 50

    # points
    circle_points = Decimal(0)
    square_points = Decimal(0)

    #
    IsRunning = True
    clock = pygame.time.Clock()
    #
    
    def calc_dist(p: tuple = (0, 0)):
        relativepos = (abs(p[0]-circle_pos[0]),abs(p[1]-circle_pos[1]))
        return Decimal(Decimal(relativepos[0]) * Decimal(relativepos[0]) + Decimal(relativepos[1]) * Decimal(relativepos[1])).sqrt()

    while IsRunning:

        # controll fps via clock
        delay = 1 / clock.tick(FPS)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IsRunning = False;

        for n in range(0, int(delay * PPS)):
            point = (random.randint(0, screen_width), random.randint(0, screen_height))

            square_points +=1
            if(calc_dist(point) < circle_radius):
                pygame.draw.rect(screen, COLOR1, (point[0], point[1], 1,1))
                circle_points += 1
            else:
                pygame.draw.rect(screen, COLOR2, (point[0], point[1], 1,1))

        pygame.display.update()

    print(f'π = {Decimal((circle_points/square_points)*Decimal(4))}')
if __name__ == "__main__":
    main()