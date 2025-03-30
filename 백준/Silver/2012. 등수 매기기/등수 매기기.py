import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = [int(input()) for _ in range(N)]
l.sort()
a = 1
p = 0
for i in range(N):
    p += abs(a-l[i])
    a += 1
print(p)