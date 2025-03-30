import sys
def input():
    return sys.stdin.readline()

n = int(input())
x,y = map(int,input().strip().split())
if n == 1:
    print(0)
else:
    if (x == n and y == 1):
        print(2)
    elif (x == n and y == n):
        print(2)
    elif (x == 1 and y == n):
        print(2)
    elif (x == 1 and y == 1):
        print(2)
    elif x == 1 or y == 1 or x == n or y == n:
        print(3)
    else:
        print(4)