import sys
def input():
    return sys.stdin.readline()

N, M, K = map(int,input().strip().split())
d = {}
l = []
p = 0
for _ in range(N):
    sub, point = input().strip().split()
    d[sub] = int(point)
    l.append(int(point))
for _ in range(K):
    sub = input().strip()
    p += d[sub]
    l.pop(l.index(d[sub]))
l.sort()
if M != K:
    print(p+sum(l[:M-K]), p+sum(l[-(M-K):]))
else:
    print(p, p)