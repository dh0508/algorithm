import sys
def input():
    return sys.stdin.readline()

MOD = 10**9 + 7

N = int(input())
l = list(map(int, input().strip().split()))

t = sum(l)
ans = 0
for i in l:
    t -= i
    ans = (ans + i * t) % MOD

print(ans)