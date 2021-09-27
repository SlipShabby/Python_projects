''''
My version of 2048 game

Logic
- 4*4 grid
- array to store values
- take cmd input from keyboard -> make move
- logic for swiping left/right or up/down
- logic to sum score in a cell and total score
- remember max score of all the games
- draw the interface
- check if the game is over

'''


import numpy as np
import random
import pygame
from pygame.locals import *


# global to store max score through all the games
BEST_SCORE = 0
N =4

# colors for future use
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (170,170,170)

# colors dict for numbers 
COLORS = {
    'background': (189, 172, 161),
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 150, 99), 
    32: (246, 124, 95),
    64: (246, 93, 59),
    128: (237, 206, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (96, 217, 146)
}

class Logic2048:
    # initialize the game and mode
    def __init__(self):
        
         # number of x/y, row/column, grid size, every cell size, margin
        self.n = 4                              
        self.cell_size = 150
        self.info_screen = 150
        self.margin = 10
        self.w = self.n*self.cell_size+(self.n+1)*self.margin
        self.h = self.w
        self.score = 0      # init score for current game
        self.best_score = BEST_SCORE

        # initialize empty array to store the grid map
        self.grid = np.zeros((self.n,self.n), dtype=int)

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


    def __str__(self):
        return str(self.grid)
    
    # insert k new numbers in random positions 
    def new_num(self, k = 1):
        # find list of indicis, storing 0
        position = list(zip(*np.where(self.grid == 0)))
        # find k positions to insert new number
        for pos in random.sample(position, k = k):
            # randomly choose to insert 2 in 90% cases
            if random.random() < .1:
                self.grid[pos] = 4
            else:
                self.grid[pos] = 2

    # helper function to sum matching numbers
    def _get_nums(self, this):
        this_n = this[this!=0]
        this_n_sum = []
        skip = False
        # delta = 0
     
        for j in range(len(this_n)):
            if skip:
                skip = False
                continue
            if j != len(this_n)-1 and this_n[j] == this_n[j+1]:
                new_n = this_n[j] *2
                skip = True
                # delta += new_n
            else:
                new_n =this_n[j]
            this_n_sum.append(new_n)
        
        return np.array(this_n_sum)

                        
        
    def make_move(self, cmd):
        print(self.grid)
        for i in range(4):
            if cmd in 'lr':
                state = self.grid[i, :]
            else:
                state = self.grid[:, i]

            transposed = False
            if cmd in 'rd':
                transposed = True
                state = state[::-1]
            
            print(state)
            state_sum = self._get_nums(state)
            new_state = np.zeros_like(state)
            new_state[:len(state_sum)] = state_sum

            if transposed:
                new_state = new_state[::-1]

            if cmd in 'lr':
                self.grid[i, :] = new_state
            else:
                self.grid[:, i] = new_state 

   
     # helper fn for input cmd input from the keyboard
    @staticmethod
    def key():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return 'q'
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        return 'u'
                    elif event.key == K_RIGHT:
                        return 'r'
                    elif event.key == K_LEFT:
                        return 'l'
                    elif event.key == K_DOWN:
                        return 'd'
                    elif event.key == K_q or event.key == K_ESCAPE:
                        return 'q'

   
    #draw pygame interface/window 
    def draw_game(self):
        # backkground color
        self.screen.fill(COLORS['background'])
        # info screen size, color
        INFO_SCREEN = pygame.Rect(0,0, self.w, 120)
        pygame.draw.rect(self.screen, WHITE, INFO_SCREEN)
        # Score sign font, color, position
        font_score = pygame.font.SysFont('simsum', 50)
        text_score = font_score.render('Score: ', True, (255,127,0))
        self.screen.blit(text_score, (30,30))

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
                                COLORS[cell], 
                                pygame.Rect(cell_x, cell_y, cell_w, cell_h), 
                                border_radius = 5)
                if cell == 0:
                    continue
                text_surface = self.myfont.render(f'{cell}', True, (0,0,0))
                text_rect = text_surface.get_rect(center = (cell_x+cell_w/2, cell_y+cell_h/2))
                self.screen.blit(text_surface, text_rect)
    

    def game_over(self):
        grid_bu = self.grid.copy()
        for move in 'lrud':
            self.make_move(move)
            if not all((self.grid == grid_bu).flatten()):
                self.grid = grid_bu
                return False
        return True

    def last_screen(self):
        pass


    def play(self):

        # init 2 first cells
        self.new_num(k = 2)

        while True:
            # fn to see the grid in terminal, before finishing thee 
            print(self.grid)
            self.draw_game()

            # update the screen 
            pygame.display.flip()
            cmd = self.key()
            if cmd == 'q':
                break

            previous_grid = self.grid.copy()
            self.make_move(cmd)
            # temporary print in terminal
            # print(game.grid)
        
            
            # if self.game_over():
            #     print('GAME OVER!')
            #     # create fn to draw game over screen
            #     # self.last_screen()
            #     break

            if not all((self.grid == previous_grid).flatten()):
                self.new_num()

if __name__ == '__main__':
    game = Logic2048()
    game.play()
