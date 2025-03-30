import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = 0
r = 0
p = 0
cnt = 0
while l <= N:
    if p > N:
        p -= l
        l += 1
    elif p < N:
        p += r
        r += 1
    elif p == N:
        cnt += 1
        p += r
        r += 1

print(cnt)