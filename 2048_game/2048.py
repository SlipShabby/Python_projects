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

import pygame
import random
import os

pygame.init()
# initialize global variables 
WIDTH, HEIGHT = 800, 900
MARGIN = 100
WHITE = (255,255,255)
BLACK = (0,0,0)
colors = [(255,255,255), (0,0,0)]
FPS = 60

val =2

# window settings: size and frequency
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My 2048 clone')


# title and icon
# icon = pygame.image.load('')
# pygame.display.set_icon(icon)

# load fonts
# pygame.font.init()
# font1 = pygame.font.SysFont('Ariel', 40)


# draw a screen window and fill it with color
def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()

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
    pygame.display.update()

def draw_value():
    text = font1.render(str(val), 1, WHITE)
    WIN.blit(text, (0,0))
    # pygame.display.flip()
    pygame.display.update()


# initiate the screen and starting point
def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
        draw_window()
        draw_grid()
        # draw_value()

    pygame.quit()

if __name__ == '__main__':
   
    main()