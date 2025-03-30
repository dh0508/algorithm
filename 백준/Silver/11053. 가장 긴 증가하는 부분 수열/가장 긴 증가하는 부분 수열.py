import sys
def input():
    return sys.stdin.readline().strip()

n = int(input())
l = list(map(int, input().split()))
dp = [1 for _ in range(n+1)]

for i in range(1, n):
    for j in range(i):
        if l[j] < l[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
