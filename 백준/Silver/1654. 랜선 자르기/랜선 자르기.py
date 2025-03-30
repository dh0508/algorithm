import sys
def input():
    return sys.stdin.readline()

k, n = map(int,input().strip().split())
kl = []
for _ in range(k):
    kl.append(int(input()))
s,e = 1, max(kl)
p = 0

while s <= e:
    nn = 0
    m = (s + e) // 2
    for i in kl:
        nn += i // m
    if nn >= n:
        p = m
        s = m + 1
    else:
        e = m - 1

print(int(p))