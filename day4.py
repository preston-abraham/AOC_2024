import numpy as np
import pandas as pd
import re
from itertools import repeat

sample_inp = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
with open("inputs/day4.txt",'r') as f:
    full_inp = f.read()
    

inp = [list(e) for e in full_inp.split('\n')]
xmax = len(inp)
ymax = len(inp[0])

s=0
for i in range(xmax):
    for j in range(ymax):
        if inp[i][j] == 'X':
            #left
            if j >= 3 and inp[i][j-1] == 'M' and inp[i][j-2] == 'A' and inp[i][j-3] == 'S':
                s+=1
            #right
            if j <= (xmax-4) and inp[i][j+1] == 'M' and inp[i][j+2] == 'A' and inp[i][j+3] == 'S':
                s+=1
            #up
            if i >= 3 and inp[i-1][j] == 'M' and inp[i-2][j] == 'A' and inp[i-3][j] == 'S':
                s+=1
            #down
            if i <= (ymax-4) and inp[i+1][j] == 'M' and inp[i+2][j] == 'A' and inp[i+3][j] == 'S':
                s+=1
            #diag left down
            if j >= 3 and i <= (ymax-4) and inp[i+1][j-1] == 'M' and inp[i+2][j-2] == 'A' and inp[i+3][j-3] == 'S':
                s+=1
            #diag left up
            if j >= 3 and i  >= 3 and inp[i-1][j-1] == 'M' and inp[i-2][j-2] == 'A' and inp[i-3][j-3] == 'S':
                s+=1
            #diag right down
            if j <= (xmax-4) and i <= (ymax-4) and inp[i+1][j+1] == 'M' and inp[i+2][j+2] == 'A' and inp[i+3][j+3] == 'S':
                s+=1
            #diag right up
            if j <= (xmax-4) and i >= 3 and inp[i-1][j+1] == 'M' and inp[i-2][j+2] == 'A' and inp[i-3][j+3] == 'S':
                s+=1

print(s)

s2 = 0

for i in range(1,xmax-1):
    for j in range(1,ymax-1):
        if inp[i][j] == 'A':
            #M M
            #S S
            if inp[i-1][j-1] == 'M' and inp[i-1][j+1] == 'M' and inp[i+1][j-1] == 'S' and inp[i+1][j+1] == 'S':
                s2 += 1
            
            #S M
            #S M
            if inp[i-1][j-1] == 'S' and inp[i-1][j+1] == 'M' and inp[i+1][j-1] == 'S' and inp[i+1][j+1] == 'M':
                s2 += 1
            
            #M S
            #M S
            if inp[i-1][j-1] == 'M' and inp[i-1][j+1] == 'S' and inp[i+1][j-1] == 'M' and inp[i+1][j+1] == 'S':
                s2 += 1
            
            #S S
            #M M
            if inp[i-1][j-1] == 'S' and inp[i-1][j+1] == 'S' and inp[i+1][j-1] == 'M' and inp[i+1][j+1] == 'M':
                s2 += 1
print(s2)
