import sys
def input():
    return sys.stdin.readline()

N, M = map(int, input().strip().split())
l = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = l[0][0]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + l[i][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + l[0][i]
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j]+l[i][j], dp[i][j-1]+l[i][j], dp[i-1][j-1]+l[i][j])
print(dp[N-1][M-1])