import sys
def input():
    return sys.stdin.readline()

MOD = 1000000007
dp = [0 for _ in range(5001)]
dp[0] = 1

for l in range(2, 5001, 2):
    for k in range(0, l - 1, 2):
        dp[l] = (dp[l] + dp[k] * dp[l - 2 - k]) % MOD



T = int(input())
for _ in range(T):
    L = int(input())
    if L % 2 == 0:
        print(dp[L])
    else:
        print(0)