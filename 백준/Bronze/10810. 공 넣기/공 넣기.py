import sys
def input():
    return sys.stdin.readline()

n, m = map(int,input().split())
p = [0 for _ in range(n)]
for _ in range(m):
    f, t, num = map(int, input().split())
    for i in range(f,1+t):
        p[i-1] = num
print(*p)