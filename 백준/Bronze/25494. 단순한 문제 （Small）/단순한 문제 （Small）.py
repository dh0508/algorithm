import sys
def input():
    return sys.stdin.readline()

T = int(input())
for _ in range(T):
    a,b,c = map(int,input().strip().split())
    p = 0
    for x in range(1,1+a):
        for y in range(1,1+b):
            for z in range(1,1+c):
                if x%y == y%z and y%z == z%x:
                    p += 1
    print(p)