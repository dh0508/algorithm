import sys
def input():
    return sys.stdin.readline()

n, x = map(int,input().strip().split())
l = []
for _ in range(n):
    l.append(list(map(int,input().strip().split())))
for i in range(n):
    if sum(l[i]) > x:
        l[i][0] = 0
l.sort()
if l[-1][0] == 0:
    print(-1)
else:
    print(l[-1][0])