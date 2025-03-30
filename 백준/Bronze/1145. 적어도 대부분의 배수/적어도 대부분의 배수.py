import sys
def input():
    return sys.stdin.readline()

l = list(map(int,input().strip().split()))
for i in range(1, 970201):
    cnt = 0
    for j in l:
        if i % j == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        exit()