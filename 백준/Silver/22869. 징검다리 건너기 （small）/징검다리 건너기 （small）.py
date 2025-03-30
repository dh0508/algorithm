import sys
def input():
    return sys.stdin.readline()

N, K = map(int,input().strip().split())
l = list(map(int,input().strip().split()))
l = [0]+l
dp = [0 for i in range(N+1)]
dp[1] = 1

for i in range(1, N):
    for j in range(i+1, 1+N):
        if dp[i] and ((j-i)*(1+abs(l[i] - l[j])) <= K):
            dp[j] = 1
if dp[-1]:
    print("YES")
else:
    print("NO")