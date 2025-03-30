import sys
def input():
    return sys.stdin.readline()

N, SL = map(int,input().strip().split())
s = list(map(int,input().strip().split()))
ans = sys.maxsize
for i in range(1,1002):
    if i in s:
        continue
    for j in range(i, 1002):
        if j in s:
            continue
        for k in range(j, 1002):
            if k in s:
                continue
            if ans > abs(N -i*j*k):
                ans = abs(N -i*j*k)
            if N < i*j*k:
                break
print(ans)