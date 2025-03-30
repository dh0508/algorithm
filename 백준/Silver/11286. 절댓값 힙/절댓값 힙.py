import sys
def input():
    return sys.stdin.readline()

import heapq
n = int(input())
l = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if l:
            print(heapq.heappop(l)[1])
        else:
            print(0)
    else:
        heapq.heappush(l, (abs(a),a))