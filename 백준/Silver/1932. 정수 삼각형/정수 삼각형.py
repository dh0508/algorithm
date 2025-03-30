import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().strip().split())))
dp = [[0 for _ in range(i+1)] for i in range(n)]
dp[0][0] = l[0][0]
for i in range(n-1):
    for j in range(len(l[i])):
        if dp[i][j] + l[i+1][j] > dp[i+1][j]:
            dp[i+1][j] = dp[i][j] + l[i+1][j]
        if dp[i][j] + l[i+1][j+1] > dp[i+1][j+1]:
            dp[i+1][j+1] = dp[i][j] + l[i+1][j+1]
print(max(dp[n-1]))