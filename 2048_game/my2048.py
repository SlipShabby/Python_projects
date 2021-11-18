from typing import NoReturn
import numpy as np
import random
import pygame
from pygame.locals import *

# import file with color pallet
import colors as COLORS

# global vars
N = 4               # grid size
BEST_SCORE = 0      # store best score of the user




# create class
class My2048:

    def __init__(self):
        self.grid = np.zeros((N,N), dtype = int)
        self.cell_size = 150
        self.info_screen = 150
        self.margin = 10
        self.w = N*self.cell_size+(N+1)*self.margin
        self.h = self.w
        self.score = 0      # init score for current game
        self.best_score = BEST_SCORE        # best score in the game
        
       # init pygame module and game title
        pygame.init()
        pygame.display.set_caption('2048')

        # init font
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Ariel', 100)

        # define game window mode; width and height
        # self.w * self.h = grid
        # set place for information screen + 150
        self.screen = pygame.display.set_mode((self.w, self.h+self.info_screen))


    def new_number(self,k=1):
        position = list(zip(*np.where(self.grid == 0)))
        for pos in random.sample(position, k = k):
            if random.random() < .1:
                self.grid[pos] = 4
            else:
                self.grid[pos] = 2
    
    
    @staticmethod
    def key():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return 'q'
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        return 'l'
                    elif event.key == K_RIGHT:
                        return 'r'
                    elif event.key == K_UP:
                        return 'u'
                    elif event.key == K_DOWN:
                        return 'd'
                    elif event.key == K_q or event.key == K_ESCAPE:
                        return 'q'
                        

    def calc(self, numbers):
        new_numbers=np.copy(numbers)
        if len(numbers) >= 2:
            for i in range(0,len(numbers)-1):
                if numbers[i] == numbers[i+1]:
                    numbers[i]*=2
                    self.score +=numbers[i]
                    new_numbers = np.delete(numbers,i+1)
                else:
                    continue
        # print('new1:\n',new_numbers, len(new_numbers))
        return new_numbers

    def make_move(self, cmd):
        if cmd in 'lr':
            grid = self.grid
        elif cmd in 'ud':
            grid = np.transpose(self.grid)

        for i in range(N):
            numbers = grid[i][np.nonzero(grid[i])]
            new = self.calc(numbers)
            if cmd in 'rd':
                grid[i] = np.pad(new, N-len(new))[0:N]
            else:
                grid[i] = np.pad(new, (0,N-len(new)))
        
        #     grid[i] = self.calc(numbers)
            # print('grid i', grid[i])

        if cmd in 'ud':
            # print('final T')
            self.grid = np.transpose(grid)

        # print('after swipe: \n',self.grid)
        # self.new_number()
        # print('+ new number: \n', self.grid)

    #draw pygame interface/window 
    def draw_game(self):
        # background color
        self.screen.fill(COLORS.GRID_COLOR)
        # info screen size, color
        INFO_SCREEN = pygame.Rect(0,0, self.w, 120)
        pygame.draw.rect(self.screen, COLORS.WHITE, INFO_SCREEN)
        # Score sign font, color, position
        font_score_label = pygame.font.SysFont(*COLORS.SCORE_LABEL_FONT)
        font_score = pygame.font.SysFont(*COLORS.SCORE_FONT)
        text_score = font_score_label.render('Score: ', True, COLORS.SCORE_LABEL)
        text_total = font_score.render(f'{self.score}', True, COLORS.SCORE)#
        self.screen.blit(text_score, (30,30))
        self.screen.blit(text_total, (200,30))

        # define grid and coords of cells to draw
        for x in range(4):
            for y in range(4):
                cell = self.grid[x][y]

                cell_x = y * self.w // 4 + self.margin
                cell_y = x * self.h // 4 + self.margin + self.info_screen
                cell_w = self.w // 4 - 2 * self.margin
                cell_h = self.h // 4 - 2 * self.margin

                # draw
                pygame.draw.rect(self.screen, 
                                COLORS.CELL_COLORS[cell], 
                                pygame.Rect(cell_x, cell_y, cell_w, cell_h), 
                                border_radius = 5)
                if cell == 0:
                    continue
                text_surface = self.myfont.render(f'{cell}', True, COLORS.CELL_NUMBER_COLORS[cell])
                text_rect = text_surface.get_rect(center = (cell_x+cell_w/2, cell_y+cell_h/2))
                self.screen.blit(text_surface, text_rect)


    def play(self):
        self.new_number(2)
        
        while True:
            self.draw_game()
            pygame.display.flip()
            cmd = self.key()
            if cmd == 'q':
                break

            self.make_move(cmd)
            self.new_number()


if __name__ == '__main__':
    game = My2048()
    game.play()
