with open("inputs/day1.txt",'r') as f:
    full_inp = f.read()

inp = list(map(lambda x:list(map(int,x.split())), full_inp.split('\n')))
l1,l2 = list(map(sorted,[[e[i] for e in inp] for i in range(2)]))

print(sum(list(map(lambda x,y: abs(x-y),l1,l2))))
print(sum(list(map(lambda x,y: x*y.count(x),l1,repeat(l2)))))
