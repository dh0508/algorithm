import sys
def input():
    return sys.stdin.readline()

p = 0
mp = 0
for _ in range(4):
    a, b = map(int,input().strip().split())
    p += b
    p -= a
    if mp < p:
        mp = p
print(mp)