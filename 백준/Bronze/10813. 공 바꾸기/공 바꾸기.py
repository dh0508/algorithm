import sys
def input():
    return sys.stdin.readline()

n, m = map(int,input().split())
p = [i for i in range(1,1+n)]
for _ in range(m):
    o, t = map(int, input().split())
    a = p[o-1]
    p[o-1] = p[t-1]
    p[t-1] = a
print(*p)