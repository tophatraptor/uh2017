import random as r
def getwalk(n):
    arr = [[0,0]]
    for _ in range(n):
        lastpos = arr[-1]
        lastpos[r.randint(0,1)] += [-1,1][r.randint(0,1)]
        arr.append(lastpos)
    return arr
