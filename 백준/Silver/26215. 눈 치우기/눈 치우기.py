import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().strip().split()))
l.sort(reverse= True)
if N == 1:
    t = l[0]
else:
    t = 0
    while l[0] >= 1:
        if l[1] >= 1:
            l[0] -= 1
            l[1] -= 1
        else:
            l[0] -= 1
        t += 1
        l.sort(reverse=True)
if t > 1440:
    print(-1)
else:
    print(t)