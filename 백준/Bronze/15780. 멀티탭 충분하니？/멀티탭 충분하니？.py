import sys
def input():
    return sys.stdin.readline()

N, K = map(int,input().strip().split())
l = list(map(int,input().strip().split()))
c = 0
for i in l:
    if i == 1:
        c += 1
    else:
        if i % 2 == 0:
            c += i//2
        else:
            c += i//2 + 1
if N <= c:
    print("YES")
else:
    print("NO")