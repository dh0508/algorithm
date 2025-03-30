import sys
def input():
    return sys.stdin.readline()

from collections import deque

n = int(input())
card = deque(i for i in range(1,1+n))
while len(card) != 1:
    card.popleft()
    card.append(card.popleft())
print(*card)