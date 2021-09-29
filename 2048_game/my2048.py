from typing import NoReturn
import numpy as np
import random
import pygame
from pygame.locals import *
import colors

N = 4

class My2048:

    def __init__(self):
        self.grid = np.zeros((N,N), dtype = int)

        # pygame.init()


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
                    new_numbers = np.delete(numbers,i+1)
                else:
                    continue
        print('new1:\n',new_numbers, len(new_numbers))
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

        print('after swipe: \n',self.grid)
        self.new_number()
        print('+ new number: \n', self.grid)
    

if __name__ == '__main__':
    game = My2048()
    game.new_number(2)
    print('start: \n', game.grid)
    # cmd = game.key()
    cmd = input('move: ')
    game.make_move(cmd)
    # game.new_number(2)
    # print(game.grid)
