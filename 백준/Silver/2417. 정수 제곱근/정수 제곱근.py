import sys
def input():
    return sys.stdin.readline()

n = int(input())

l, r = 0, n

while l <= r:
    m = (l+r) // 2
    if m ** 2 < n:
        l = m+1
    else:
        r = m-1

print(l)