import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().strip().split()))

cnt = 0
while len(l) > 0:
    s = set(sorted(l))
    for i in s:
        l.pop(l.index(i))
    cnt += 1

print(cnt)