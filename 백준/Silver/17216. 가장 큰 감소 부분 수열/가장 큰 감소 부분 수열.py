import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int, input().strip().split()))

dp = l.copy()
for i in range(N):
    for j in range(i):
        if l[i]<l[j]:
            dp[i] = max(dp[j]+l[i], dp[i])
print(max(dp))