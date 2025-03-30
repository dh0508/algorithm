import sys
def input():
    return sys.stdin.readline()

n = int(input())
dp = [False for i in range(10001)]
dp[3] = 1
dp[5] = 1
for i in range(1,1+n):
    if dp[i]:
        for j in range(i, 1+n):
            if dp[j]:
                if dp[i+j]:
                    if dp[i+j] > dp[i]+dp[j]:
                        dp[i + j] = dp[i] + dp[j]
                else:
                    dp[i + j] = dp[i] + dp[j]
if dp[n]:
    print(dp[n])
else:
    print(-1)