import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = list(input().strip().split())
d = {index + 1: value for index, value in enumerate(l)}
m, k = map(int,input().strip().split())
pl = []
for _ in range(m):
    subl = list(map(int,input().strip().split()))
    subl = [d[i] for i in subl]
    if 'P' in subl:
        pl.append('P')
    else:
        pl.append('W')
if 'W' in pl:
    print('W')
else:
    print('P')