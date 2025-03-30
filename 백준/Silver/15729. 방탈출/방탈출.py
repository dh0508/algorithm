import sys
def input():
    return sys.stdin.readline().strip()

def turn(l, i):
    if l[i] == 0:
        l[i] = 1
    elif l[i] == 1:
        l[i] = 0
    try:
        if l[i+1] == 0:
            l[i+1] = 1
        elif l[i+1] == 1:
            l[i+1] = 0
    except:
        pass
    try:
        if l[i+2] == 0:
            l[i+2] = 1
        elif l[i+2] == 1:
            l[i+2] = 0
    except:
        pass

N = int(input())
l = list(map(int, input().split()))
ll = [0 for _ in range(N)]
cnt = 0
for i in range(N):
    if l[i] != ll[i]:
        cnt += 1
        turn(ll,i)
print(cnt)