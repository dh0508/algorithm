import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().strip().split()))

lsort, rsort = 0, 0
ltmp, rtmp = 0, 0
for i in l:
    if i % 2 == 1:
        ltmp += 1
        lsort += rtmp
    else:
        rtmp += 1
        rsort += ltmp

print(min(lsort, rsort))