import sys
def input():
    return sys.stdin.readline()

import math
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    i = int((-1 + math.sqrt(1 + 4 * ((N - 1) * 2 / K))) / 2)
    direction = ""
    loc = 0
    length = (i * (i + 1) * K) // 2
    if i % 2 == 1:
        direction = 'L'
        loc = (i // 2 + 1) * K - (N - 1 - length)
    else:
        direction = 'R'
        loc = -(i // 2) * K + (N - 1 - length)
    print(loc, direction)