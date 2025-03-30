import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = []
for i in range(N):
    a = list(map(int, input().split()))
    a.pop(0)
    l.append(sum(a))
l.sort()
p = 0
for i in range(N):
    p += l[i] * (N-i)
print(p)