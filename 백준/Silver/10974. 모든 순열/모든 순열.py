import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = []

def solution():
    if len(l) == N:
        print(*l)
        return
    else:
        for i in range(1, 1+N):
            if i not in l:
                l.append(i)
                solution()
                l.pop()
solution()