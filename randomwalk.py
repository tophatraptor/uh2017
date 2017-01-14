import random as r
def getwalk(n):
    arr = [(0,0)]
    for i in range(0,n):
        lastpos = [arr[i][0], arr[i][1]]
        lastpos[r.randint(0,1)] += [-1,1][r.randint(0,1)]
        arr += [(lastpos[0], lastpos[1])]
    return arr
