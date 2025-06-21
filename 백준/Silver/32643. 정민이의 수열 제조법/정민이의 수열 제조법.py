import sys
def input():
    return sys.stdin.readline()

N, M = map(int, input().strip().split())

is_prime = [True for _ in range(N+1)]
is_prime[0] = False
for i in range(2, int(N**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, N+1, i):
            is_prime[j] = False

dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    dp[i] = dp[i-1] + is_prime[i]


for _ in range(M):
    a, b = map(int, input().strip().split())
    print(dp[b]-dp[a-1])