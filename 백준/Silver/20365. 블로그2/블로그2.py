import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(input().strip())
bcnt = 0
rcnt = 0
currentcolor = l[0]
for i in range(1, N):
    if l[i] != currentcolor:
        if currentcolor == 'B':
            bcnt += 1
        else:
            rcnt += 1
        currentcolor = l[i]
if l[-1] == 'B':
    bcnt += 1
else:
    rcnt += 1
print(1+min(bcnt,rcnt))