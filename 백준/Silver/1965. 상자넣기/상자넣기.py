import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = list(map(int,input().strip().split()))

dp = [1 for _ in range(n)]


for i in range(1, n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], 1+dp[j])

print(max(dp))