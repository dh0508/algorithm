import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().strip().split()))
p = -1
for i in range(N+1):
    t = l.count(i)
    if t == i:
        p = max(p,i)
print(p)