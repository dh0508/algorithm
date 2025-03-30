import sys
def input():
    return sys.stdin.readline()

D, K = map(int,input().strip().split())
dp = [0 for _ in range(D + 2)]
dp[3] = 1
dp[4] = 1
for i in range(5, D + 2):
    dp[i] = dp[i - 1] + dp[i - 2]
for a in range(1, K//2//D + 1):
    b = (K - dp[D]*a)/dp[D+1]
    if b == int(b):
        print(a, int(b), sep="\n")
        exit()