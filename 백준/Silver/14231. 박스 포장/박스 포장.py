import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int, input().split()))
l = [0] + l
dp = [0 for _ in range(N+1)]

max_val = 0
for i in range(1, N+1):
    dp[i] = 1
    for j in range(1, i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    max_val = max(max_val, dp[i])

print(max_val)