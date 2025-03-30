import sys
def input():
    return sys.stdin.readline()

N = int(input())
xl = []
yl = []
for _ in range(N):
    x, y = map(int,input().strip().split())
    xl.append(x)
    yl.append(y)
xl.sort()
yl.sort()
x = xl[N//2]
y = yl[N//2]
p = 0
for i in range(N):
    p += abs(x-xl[i])
    p += abs(y-yl[i])
print(p)