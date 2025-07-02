import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int, input().strip().split()))

cnt = 0
for i in range(N):
    if i == 0:
        cnt += 1
    elif l[i] == l[i-1]:
        cnt += 1
    else:
        for _ in range(cnt):
            print(i+1, end=' ')
        cnt = 1

for _ in range(cnt):
    print(-1, end=' ')