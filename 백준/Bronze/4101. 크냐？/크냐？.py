import sys
def input():
    return sys.stdin.readline()

while True:
    f, s = map(int,input().strip().split())
    if f == 0 and s == 0:
        break
    elif f > s:
        print('Yes')
    else:
        print('No')