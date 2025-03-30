import sys
def input():
    return sys.stdin.readline()

n, m = map(int,input().strip().split())
l = list(map(int,input().strip().split()))
if n == 0:
    print(0)
    exit()
else:
    cnt = 1
    box = 0
    while l:
        if box + l[0] > m:
            cnt += 1
            box = 0
        else:
            box += l.pop(0)
    print(cnt)