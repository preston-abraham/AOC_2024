with open("inputs/day1.txt",'r') as f:
    full_inp = f.read()

inp = [i.split('   ') for i in full_inp.split('\n')]
inp = [[int(i) for i in j] for j in inp]
l1 = sorted([e[0] for e in inp])
l2 = sorted([e[1] for e in inp])

s = 0
for i in range(len(l2)):
    s+= abs(l1[i] - l2[i])
print(s)

s2 = 0
for e in l1:
    sc = 0
    for e2 in l2:
        if e == e2:
            sc += e
    s2 += sc
print(s2)
