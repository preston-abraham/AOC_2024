import numpy as np
import pandas as pd
import re
from itertools import repeat
import itertools

sample_inp = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
with open("inputs/day10.txt",'r') as f:
    full_inp = f.read()
    
inp = sample_inp

trails = list(map(list, inp.split('\n')))
xmax = len(trails)
ymax = len(trails[0])



def neighbors(point):
    n = []
    x,y = point
    height = int(trails[x][y])
    if point[0] >= 1 and trails[x-1][y] == str(height+1):
        n += [(x-1,y)]
    if point[1] >= 1 and trails[x][y-1] == str(height+1):
        n += [(x,y-1)]
    if point[0] < xmax-1 and trails[x+1][y] == str(height+1):
        n += [(x+1,y)]
    if point[1] < ymax-1 and trails[x][y+1] == str(height+1):
        n += [(x,y+1)]
    return n

def dfs(start,p2 = False):
    score = 0
    visited = set()
    visitedList = [[]]
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            if int(trails[node[0]][node[1]]) == 9:
                score += 1
                
            for neighbor in neighbors(node):
                stack.append(neighbor)
        visitedList.append(visited)
        
        
        
    if p2:
        print(([e for e in visitedList if len(e) == 10]))
    return score

s = 0

for i in range(xmax):
    for j in range(ymax):
        if int(trails[i][j]) == 0:
            s += dfs((i,j))
print(s)           
            

s2 = 0

for i in range(xmax):
    for j in range(ymax):
        if int(trails[i][j]) == 0:
            s2 += dfs((i,j),True)
print(s2)        
