import sys
def input() :
    return sys.stdin.readline().strip()

while True:
    N = int(input())
    if N == 0:
        exit()
    else:
        l = []
        dp = [0 for i in range(N)]
        for i in range(N):
            l.append(int(input()))
        for i in range(N):
            dp[i] = max(dp[i-1]+l[i], l[i])
        print(max(dp))