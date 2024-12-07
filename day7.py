import numpy as np
import pandas as pd
import re
from itertools import repeat

sample_inp = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
with open("inputs/day7.txt",'r') as f:
    full_inp = f.read()
    
lines = full_inp.split('\n')

def valid_line(line, p2 = False):
    target,nums = line.split(': ')
    nums = list(map(int,nums.split(' ')))
    #ops = ['+','*']
    possibilities = [nums[0]]
    for i in range(1,len(nums)):
        new_possibilities = []
        for p in possibilities:
            new_possibilities += [p+nums[i],p*nums[i]]
            if p2:
                new_possibilities += [int(str(p)+str(nums[i]))]
        possibilities = new_possibilities
    
    if int(target) in possibilities:
        return int(target)
    return 0
    
print(sum(map(valid_line,lines,repeat(False))))
print(sum(map(valid_line,lines,repeat(True))))
