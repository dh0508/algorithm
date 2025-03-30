import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().strip().split()))
ll = [0 for _ in range(N)]
for i in range(N):
    a = l[i]
    for j in range(N):
        if a == 0:
            if ll[j] == 0:
                ll[j] = i+1
                break
        else:
            if ll[j] == 0:
                a -= 1
print(*ll)