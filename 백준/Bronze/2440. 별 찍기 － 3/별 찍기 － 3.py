import sys
def input():
    return sys.stdin.readline()

N = int(input())
for i in range(N, 0, -1):
    print('*'*i)