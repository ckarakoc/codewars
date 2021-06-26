from copy import deepcopy
import sys

def get_generation(cells, generations):
    if len(cells) == 0:
        return []

    curr_gen = deepcopy(cells)
    next_gen = deepcopy(cells)
    for _ in range(0, generations):
        next_gen = grow(next_gen, 1)  
        curr_gen = deepcopy(next_gen) 
        for x in range(0, len(curr_gen)):
            for y in range(0, len(curr_gen[x])):
                    count = count_neighbours(curr_gen, x, y)
                    if curr_gen[x][y] == 1: # Alive
                        if count < 2 or count > 3:
                            next_gen[x][y] = 0 # Dies
                    elif count == 3: # Dead 
                        next_gen[x][y] = 1 # Revives              
        next_gen = trim(next_gen)
    return next_gen

def grow(arr, n):
    row = len(arr) + 2*n
    col = len(arr[0]) + 2*n
    res = [[0 for _ in range(col)] for _ in range(row)]
    for x in range(n, len(res) - n):
        for y in range(n, len(res[0]) - n):
            res[x][y] = arr[x-n][y-n]
    return res
    
def trim(arr):
    minRow, minCol, maxRow, maxCol = sys.maxsize, sys.maxsize, 0, 0
    
    for row in range(0, len(arr)):
        for col in range(0, len(arr[0])):
            if arr[row][col] == 1:
                if row < minRow: 
                    minRow = row
                if row > maxRow:
                    maxRow = row
                if col < minCol:
                    minCol = col
                if col > maxCol:
                    maxCol = col
    
    return [[arr[row][col] for col in range(minCol, maxCol+1)] for row in range(minRow, maxRow+1)]

def count_neighbours(cells, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x+i < len(cells) and 0 <= y+j < len(cells[x+i]):
                sum += cells[x+i][y+j]
    return sum - cells[x][y]

def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<:LF:>')
    return ''.join(s)