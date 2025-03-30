import sys
def input():
    return sys.stdin.readline()

from collections import deque

n, m = map(int,input().strip().split())
a = deque(map(int, input().strip().split()))
b = deque(map(int, input().strip().split()))
p = []
while a and b:
    if a[0] > b[0]:
        p.append(b.popleft())
    else:
        p.append(a.popleft())
p.extend(a+b)
print(*p)