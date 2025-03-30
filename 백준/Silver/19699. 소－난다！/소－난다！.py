import sys
def input():
    return sys.stdin.readline()

from itertools import combinations

prime_l = [False, False] + [True for _ in range(9001)]
for i in range(2, int(9001**0.5)+1):
    if prime_l[i]:
        for j in range(i*i, 9001, i):
            prime_l[j] = False

N, M = map(int,input().strip().split())
l = list(map(int,input().strip().split()))

ans_prime_l = []

for i in combinations(l, M):
    if prime_l[sum(i)]:
        ans_prime_l.append(sum(i))

ans_prime_l = list(set(ans_prime_l))
ans_prime_l.sort()
if ans_prime_l:
    print(*ans_prime_l)
else:
    print(-1)