import numpy as np
import pandas as pd
import re
from itertools import repeat

sample_inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


with open("inputs/day2.txt",'r') as f:
    full_inp = f.read()
    
inp = list(map(lambda x:list(map(int,x.split())), sample_inp.split('\n')))

def safe(l, p2 = False):
    prev = l[0]
    for i in range(1,len(l)):
        if ((l[1] > l[0]) and (l[i] <= prev or l[i] - 3 > prev)) or ((l[1] < l[0]) and (l[i] >= prev or l[i] + 3 < prev)):
            if p2:
                for i in range(len(l)):
                    if safe(l[:i] + l[i+1:],False):
                        return 1
            return 0
        prev = l[i]
    return 1

print(sum(list(map(safe,inp,repeat(False)))))
print(sum(list(map(safe,inp,repeat(True)))))
