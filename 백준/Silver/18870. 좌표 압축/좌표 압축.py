import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = list(map(int,input().strip().split()))
ll = sorted(list(set(l)))
d = {ll[i]: i for i in range(len(ll))}
for i in l:
    print(d[i], end= ' ')