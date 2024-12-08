import numpy as np
import pandas as pd
import re
from itertools import repeat
import itertools

sample_inp = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
with open("inputs/day8.txt",'r') as f:
    full_inp = f.read()
    
lab = list(map(list, full_inp.split('\n')))
lab
xmax = len(lab)
ymax = len(lab[0])
signals = {}

for i in range(xmax):
    for j in range(ymax):
        if lab[i][j] != '.':
            if lab[i][j] in signals.keys():
                signals[lab[i][j]] += [(i,j)]
            else:
                signals[lab[i][j]] = [(i,j)]
def antinodes(points, p2 = False):
    point1, point2 = points
    xs = [point1[0],point2[0]]
    ys = [point1[1],point2[1]]
    an = [[xs[0] - (xs[1] - xs[0]), ys[0] - (ys[1] - ys[0])],[xs[1] + (xs[1] - xs[0]), ys[1] + (ys[1] - ys[0])]]
    
    if p2:
        for i in range(xmax):
            an += [xs[0] - i*(xs[1] - xs[0]), ys[0] - i*(ys[1] - ys[0])],[xs[1] + i*(xs[1] - xs[0]), ys[1] + i*(ys[1] - ys[0])]
    
    return([e for e in an if (e[0] >= 0 and e[0] < xmax and e[1] >= 0 and e[1] < ymax)])
print(antinodes(((5,6),(3,4))))

nodes = []
for s in signals.keys():
    n = list(map(antinodes,itertools.combinations(signals[s],2),repeat(False)))
    n = [e for e2 in n for e in e2]
    nodes += n
print(len(list(set(map(str,nodes)))))
nodes = []
for s in signals.keys():
    n = list(map(antinodes,itertools.combinations(signals[s],2),repeat(True)))
    n = [e for e2 in n for e in e2]
    nodes += n
print((len(list(set(map(str,nodes))))))
