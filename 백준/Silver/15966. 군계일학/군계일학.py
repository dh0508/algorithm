import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int, input().strip().split()))

dp = [0 for _ in range(1000001)]

for i in range(N):
    tmp = l[i]
    if tmp==0:
        pass
    else:
        dp[tmp] = max(dp[tmp], dp[tmp-1]+1)
print(max(dp))