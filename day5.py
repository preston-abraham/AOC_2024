import numpy as np
import pandas as pd
import re
from itertools import repeat

sample_inp = """""
with open("inputs/day5.txt",'r') as f:
    full_inp = f.read()
    
inp = full_inp
rules,pages = inp.split('\n\n')
rules = list(map(lambda x: x.split('|'), rules.split('\n')))

pages = list(map(lambda x: x.split(','), pages.split('\n')))

def reorder_page(page):
    seen = []
    relevant_rules = [r for r in rules if r[0] in page and r[1] in page]
    for _ in range(len(page)): # not incredibly proud of this work-around
        for r in relevant_rules:
            i0 = page.index(r[0])
            i1 = page.index(r[1])
            if  i0 > i1:
                page[i0] = r[1]
                page[i1] = r[0]
    return page

def valid_page(page,p2):
    seen = []
    for p in page:
        for r in rules:
            if r[0] == p and r[1] in seen:
                if p2:
                    new_page = reorder_page(page)
                    return int(new_page[int((len(new_page) - 1) / 2)])
                return 0
        seen += [p]
    if p2:
        return 0
    return int(page[int((len(page) - 1) / 2)])

print(sum(map(valid_page,pages,repeat(False))))
print(sum(map(valid_page,pages,repeat(True))))
