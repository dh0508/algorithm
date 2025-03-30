import sys
def input():
    return sys.stdin.readline()

N, K = map(int,input().strip().split())
dp = [[1 for j in range(i+1)] for i in range(N+1)]
for i in range(N+1):
    for j in range(i+1):
        if j == 0 or j == i:
            pass
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1] % 10007
print(dp[N][K] % 10007)