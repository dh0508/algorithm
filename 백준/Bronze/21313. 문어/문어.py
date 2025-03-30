import sys
def input():
    return sys.stdin.readline()

N = int(input())
if N % 2 == 0:
    for i in range(1,N):
        if i % 2 == 0:
            print(2, end= ' ')
        else:
            print(1, end=' ')
    print(2)
else:
    for i in range(1, N):
        if i % 2 == 0:
            print(2, end=' ')
        else:
            print(1, end=' ')
    print(3)