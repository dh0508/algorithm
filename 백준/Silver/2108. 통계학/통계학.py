import sys
def input():
    return sys.stdin.readline()

from math import ceil, floor

n = int(input())
l = []
ll = [0 for _ in range(8001)]
for _ in range(n):
    l.append(int(input()))

print(round(sum(l)/n))

l.sort()
print(l[n//2])

for i in l:
    ll[i+4000] += 1
if ll.count(max(ll)) >= 2:
    ll[ll.index(max(ll))] = 0
    print(ll.index(max(ll)) - 4000)
else:
    print(ll.index(max(ll))-4000)

print(max(l)-min(l))