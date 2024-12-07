import numpy as np
import pandas as pd
import re
from itertools import repeat

sample_inp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
with open("inputs/day6.txt",'r') as f:
    full_inp = f.read()

lab = list(map(lambda x: list(x),full_inp.split('\n')))

lab
xmax = len(lab)
ymax = len(lab[0])
start = []
current_dir = ''
dirs = {'^':[-1,0],'>':[0,1],'v':[1,0],'<':[0,-1]}
dir_list = ['^','>','v','<']
visited = []
visited_with_dir = []

for i in range(xmax):
    for j in range(ymax):
        if lab[i][j] not in ['#','.']:
            start = [i,j]
            current_dir = lab[i][j]
            break

pos = start

potential_loop_blockers = 0

while True:
    visited += [str(pos)]
    visited_with_dir += [str([pos,current_dir])]
    next_pos = [pos[0] + dirs[current_dir][0], pos[1] + dirs[current_dir][1]]
    
    if next_pos[0] < 0 or next_pos[0] >= xmax or next_pos[1] < 0 or next_pos[1] >= ymax:
        break
    if lab[next_pos[0]][next_pos[1]] != '#':
        
        if lab[next_pos[0]][next_pos[1]] == '.':
            blocker_dir = dir_list[(dir_list.index(current_dir) + 1) % 4]
            blocker_pos = pos
            while True:
                blocker_next_pos = [blocker_pos[0] + dirs[blocker_dir][0], blocker_pos[1] + dirs[blocker_dir][1]]

                if blocker_next_pos[0] < 0 or blocker_next_pos[0] >= xmax or blocker_next_pos[1] < 0 or blocker_next_pos[1] >= ymax:
                    break
                if lab[blocker_next_pos[0]][blocker_next_pos[1]] == '#':
                    break
                if str([blocker_next_pos,blocker_dir]) in final_path:
                    potential_loop_blockers += 1
                    break
                blocker_pos = blocker_next_pos
                
        pos = next_pos
        
        continue
    if lab[next_pos[0]][next_pos[1]] == '#':
        current_dir = dir_list[(dir_list.index(current_dir) + 1) % 4]
        continue
    
    
print(len(list(set(visited))))
print(potential_loop_blockers)
