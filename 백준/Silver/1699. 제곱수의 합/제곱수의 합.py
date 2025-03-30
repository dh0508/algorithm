import sys
def input():
    return sys.stdin.readline().strip()

n = int(input())
dp = [i for i in range(100001)]
for i in range(1,n+1):
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
print(dp[n])