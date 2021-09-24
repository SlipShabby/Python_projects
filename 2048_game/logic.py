''''
My logic for 2048

1 create 2D array 4*4
2 create arrr to store the val of the grid
'''


import numpy as np

l = np.zeros((4,4),dtype=int)
print(l)

def print_grid(l):
    print('*' * 20)
    for i in l:
        print(*i)
    print('*'*20)

def init_grid(l):
    grid = []
    for x in range(4):
        for y in range(4):
            if l[x][y] == 0:
                num = num_ind(x,y)
                grid.append(num)
    return grid


def num_ind(i,j):
    return 4*i + j+1

l[0][2] = 2
l[1][3] = 4
print(init_grid(l))
print_grid(l)
