import numpy as np
import pandas as pd
import re
from itertools import repeat
import itertools

sample_inp = """2333133121414131402"""
with open("inputs/day9.txt",'r') as f:
    full_inp = f.read()
    
inp = full_inp

inp = list(map(int,list(inp)))

def spread(inp):
    res = []
    current_index = 0
    for i in range(len(inp)):
        if not i % 2:
            res += [current_index for i in range(inp[i])]
            current_index += 1
        else:
            res += ['.' for i in range(inp[i])]
    return res
def wrap(spread):
    spread_rev = [e for e in spread if not e == '.'][::-1]
    count_swaps = 0
    for i in range(len(spread)):
        if spread[i] == '.':
            spread[i] = spread_rev[count_swaps]
            count_swaps += 1
    spread = spread[:-count_swaps]
    return spread

def move_files(inp):
    slots = inp[1::2]
    file_sizes = inp[::2]
    files = [i for i in range(len(file_sizes))]
    moves = []
    
    for i in files[::-1]:
        for j in range(i):
            if file_sizes[i] <= slots[j]:
                slots[j] -= file_sizes[i]
                moves += [(j,i,file_sizes[i])]
                break
    
    move_keys = {f:[] for f in files}
    for e in sorted(moves,key = lambda x:x[0]):
        for _ in range(e[2]):
            move_keys[e[0]] += [e[1]]
            
            
    spread_inp = spread(inp)
    most_recent_num  = 0
    moved = []
    for i in range(len(spread(inp))):
        if spread_inp[i] == '.':
            if move_keys[most_recent_num] != []:
                replacement = move_keys[most_recent_num][0]
                move_keys[most_recent_num] = move_keys[most_recent_num][1:]
                spread_inp[i] = replacement
                moved += [spread_inp[i]]
        else:
            most_recent_num = spread_inp[i]
            if spread_inp[i] in moved:
                spread_inp[i] = '.'
    return(spread_inp)

def checksum(inp):
    inp = [e if e != '.' else 0 for e in inp]
    return sum(i*j for i,j in enumerate(inp))

  
print(checksum(wrap(spread(inp))))
print(checksum(move_files(inp)))
