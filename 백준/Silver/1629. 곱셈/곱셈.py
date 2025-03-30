import sys
def input():
    return sys.stdin.readline()

a, b, c = map(int,input().strip().split())

def power(a,b):
    if b == 0:
        return 1
    x = power(a,b//2)
    if b % 2 == 0:
        return x*x%c
    else:
        return x*x*a%c

print(power(a,b))