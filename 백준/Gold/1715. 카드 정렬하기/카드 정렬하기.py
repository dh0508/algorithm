import sys
def input():
    return sys.stdin.readline()

from queue import PriorityQueue
N = int(input())
l = PriorityQueue()
for _ in range(N):
    l.put(int(input()))
p = 0
for _ in range(N-1):
    a = l.get(0)
    b = l.get(0)
    l.put(a+b)
    p += a+b
print(p)