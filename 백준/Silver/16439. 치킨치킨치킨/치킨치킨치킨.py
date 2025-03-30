import sys
def input():
    return sys.stdin.readline()


N, M = map(int,input().strip().split())
l = [[]for _ in range(M)]

for i in range(N):
    ll = list(map(int,input().strip().split()))
    for j in range(M):
        l[j].append(ll[j])
p = 0
for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1, M):
            lll = []
            for ii in range(N):
                lll.append(max(l[i][ii], l[j][ii], l[k][ii]))
            p = max(sum(lll), p)
print(p)