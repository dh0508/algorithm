import sys
def input():
    return sys.stdin.readline()

N, b = map(int, input().strip().split())
if 2**(b+1)-1 >= N:
    print('yes')
else:
    print('no')