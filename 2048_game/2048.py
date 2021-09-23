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


WIDTH, HEIGHT = 600, 900
WHITE = (255,255,255)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My 2048 clone')

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()


def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()

if __name__ == '__main__':
    main()