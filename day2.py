import numpy as np
import pandas as pd
import re

sample_inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


with open("inputs/day2.txt",'r') as f:
    full_inp = f.read()
    
inp = [i.split(' ') for i in  full_inp.split('\n')]
inp = [[int(i) for i in j] for j in inp]

def safe(l):
    if l[1] > l[0]:
        prev = l[0]
        for i in range(1,len(l)):
            if l[i] <= prev or l[i] - 3 > prev:
                return False
            prev = l[i]
    else:
        prev = l[0]
        for i in range(1,len(l)):
            if l[i] >= prev or l[i] + 3 < prev:
                return False
            prev = l[i]
    return True

s = 0
for ls in inp:
    if safe(ls):
        s+=1
print(s)

s2 = 0
for ls in inp:
    if safe(ls):
        s2+=1
    else:
        for i in range(len(ls)):
            if safe(ls[:i] + ls[i+1:]):
                s2 += 1
                break
                
print(s2)
