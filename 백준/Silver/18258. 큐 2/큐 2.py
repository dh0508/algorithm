import sys
def input():
    return sys.stdin.readline()

from collections import deque
l = deque()

N = int(input())

for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        l.append(int(order[1]))

    elif order[0] == 'pop':
        if not l:
            print(-1)
        else:
            print(l[0])
            l.popleft()

    elif order[0] == 'size':
        print(len(l))

    elif order[0] == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if not l:
            print(-1)
        else:
            print(l[0])

    elif order[0] == 'back':
        if not l:
            print(-1)
        else:
            print(l[-1])