import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().strip().split()))

d = {}
cnt = 0

for i in l:
    if i in d and d[i] > 0:
        d[i] -= 1
    else:
        cnt += 1
    if i-1 in d:
        d[i-1] += 1
    else:
        d[i-1] = 1

print(cnt)