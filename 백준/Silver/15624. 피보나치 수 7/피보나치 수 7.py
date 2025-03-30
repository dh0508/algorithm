import sys
def input():
    return sys.stdin.readline()

n = int(input())
if n != 0:
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = (dp[i-1]+dp[i-2] % 1000000007)
    print(dp[n] % 1000000007)
else:
    print(0)