# my implementation of 2048 game
''''
Steps:
1 create 4*4 grid, with initially 2 cells filled with 2 random numbers.
2 user pass cmds to simulate swipe 
    cmds: up, down, left, right
3 so cells values adds up, moved cell become empty
4 2 random cells are filled with 2 random numbers
5 the goal is to reach 2048 value
    - goal reached: win!
    - if goal is not reached and there is no 2 cells to be filled with 2 new cells: game over!

'''

import os
import pygame
import random

from sys import exit
from pygame import image

pygame.init()

WIDTH, HEIGHT = 800, 900
MARGIN = 100
# window settings: size and frequency
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My 2048 clone')


# initialize global variables 

WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60

# pygame.font.init()
# pygame.mixer.init()
font1 =pygame.font.SysFont('Ariel',80)


# image1 = pygame.image.load(os.path.join('2048_game/assets', 'logo.png'))


# title and icon
# icon = pygame.image.load('')
# pygame.display.set_icon(icon)


# draw a screen window and fill it with color
def draw_window():
    WIN.fill(BLACK)
    # WIN.blit(image1, (300,300))
    first_num = font1.render('2048', 1, WHITE)
    WIN.blit(first_num, (10, 10))
  

# draw grid (4 x 4) and initialize array to store the values
def draw_grid():
    grid_size = 150
    grid = []
    for x in range(4):
        grid.append([])
        for y in range(4):
            grid[x].append([])
            rect = pygame.Rect(x*grid_size + MARGIN, y*grid_size + MARGIN, grid_size, grid_size)
            pygame.draw.rect(WIN, WHITE, rect,10)
    # test value
    
    # return x,y



# initiate the screen and starting point
def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
        draw_window()
        draw_grid()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    exit()

if __name__ == '__main__':
   
    main()