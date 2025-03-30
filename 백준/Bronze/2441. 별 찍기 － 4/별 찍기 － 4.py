import sys
def input():
    return sys.stdin.readline()

N = int(input())
for i in range(N):
    print(' ' * i + '*' * (N-i))