import sys
def input():
    return sys.stdin.readline()

a, b = map(int,input().strip().split())
print(a*b)