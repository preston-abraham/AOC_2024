import numpy as np
import pandas as pd
import re
from itertools import repeat

sample_inp = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5)"""
sample_inp_p2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
sample_inp_p3 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))do()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
with open("inputs/day3.txt",'r') as f:
    full_inp = f.read()
  
inp = full_inp

pairs = re.findall('mul\([0-9]*,[0-9]*\)',inp)
print(sum(list(map(lambda x: x[0]*x[1], list(map(lambda x: list(map(int,(x[4:-1]).split(','))),pairs))))))

inp = re.sub(r"don't\(\).+?do\(\)", "", inp, flags=re.DOTALL)
pairs = re.findall('mul\([0-9]*,[0-9]*\)',inp)
print(sum(list(map(lambda x: x[0]*x[1], list(map(lambda x: list(map(int,(x[4:-1]).split(','))),pairs))))))
