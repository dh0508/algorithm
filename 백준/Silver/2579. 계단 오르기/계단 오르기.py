import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = [0]
for _ in range(n):
    l.append(int(input()))
l += [0,0,0,0]
dp = [0 for _ in range(301)]
dp[1] = l[1]
dp[2] = l[1] + l[2]
dp[3] = max(l[1] + l[3], l[2] + l[3])
for i in range(4,n+1):
    dp[i] = max(dp[i-3]+l[i-1]+l[i], dp[i-2]+l[i])
print(dp[n])