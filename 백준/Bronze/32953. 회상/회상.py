import sys
def input():
    return sys.stdin.readline()

N, M = map(int,input().strip().split())
l = []
for _ in range(N):
    K = int(input())
    l += list(map(int, input().strip().split()))
d = {}
for i in range(len(l)):
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1
cnt = 0
for key, value in d.items():
    if value >= M:
        cnt += 1
print(cnt)