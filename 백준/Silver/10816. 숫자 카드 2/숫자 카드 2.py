import sys
def input():
    return sys.stdin.readline()

n = int(input())
nl = list(map(int,input().strip().split()))
m = int(input())
ml = list(map(int,input().strip().split()))
nd = {}
for i in nl:
    if i in nd:
        nd[i] += 1
    else:
        nd[i] = 1
pl = []
for i in ml:
    try:
        pl.append(nd[i])
    except:
        pl.append(0)
print(*pl)