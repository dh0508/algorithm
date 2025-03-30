import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().strip().split()))
l.sort()
v = float("inf")
for i in range(N):
    a = l[i]
    if v <= (- sum(l[:i]) + sum(l[i:]) + a*(i+1) - a*(N-i+1)) and l[i] != l[i-1]:
        print(l[i-1])
        exit()
    v = - sum(l[:i]) + sum(l[i:]) + a*(i+1) - a*(N-i+1)
print(l[-1])