import sys
def input():
    return sys.stdin.readline()

N, K = map(int,input().strip().split())
l = [float(input()) for _ in range(N)]
l.sort()
print(f"{sum(l[K:N-K]) / (N - 2 * K) + 0.00000001:.2f}")
for i in range(K):
    l[i] = l[K]
for i in range(K):
    l[-i-1] = l[-(K+1)]
print(f"{sum(l) / N + 0.00000001:.2f}")