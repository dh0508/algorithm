import sys
def input():
    return sys.stdin.readline()

N = int(input())
for i in range(N):
    spaces = (2 * N - 1 - (1 + 2 * i)) // 2
    print(' ' * spaces + '*' * (1 + 2 * i))
