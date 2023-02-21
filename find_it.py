from collections import defaultdict

def find_it(seq):
    d = defaultdict(int)
    for i in seq:
        d[i] += 1
    for i,j in d.items():
        if j%2 == 1:
            return i
