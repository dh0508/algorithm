import sys
def input():
    return sys.stdin.readline()

sys.setrecursionlimit(10**9)
N, P, Q, X, Y = map(int,input().strip().split())
dp = {}
dp[0] = 1
def solution(i):
    if i in dp:
        return dp[i]
    if i<0 :
        return 1
    dp[i] = solution(int(i/P)-X) + solution(int(i/Q)-Y)
    return dp[i]

print(solution(N))