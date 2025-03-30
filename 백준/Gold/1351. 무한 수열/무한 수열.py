import sys
def input():
    return sys.stdin.readline()

sys.setrecursionlimit(10**9)
N, P, Q = map(int,input().strip().split())
dp = {}
dp[0] = 1
def solution(i):
    if i in dp:
        return dp[i]
    dp[i] = solution(int(i/P)) + solution(int(i/Q))
    return dp[i]

print(solution(N))