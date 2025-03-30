import sys
def input():
    return sys.stdin.readline()
n = int(input())
l = list(map(int,input().strip().split()))
dp = [0] + l
dp[1] = l[0]
for i in range(1+n):
    for j in range(1,i):
        dp[i] = max(dp[i], dp[i-j]+l[j-1])

print(dp[n])