import sys
def input():
    return sys.stdin.readline()

N = int(input())
dp = [0 for _ in range(20+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
for i in range(5, N+1):
    if i % 2 == 0:
        dp[i] = dp[i-1]*2 - dp[i-4] - dp[i-5]
    else:
        dp[i] = dp[i-1]*2
print(dp[N])