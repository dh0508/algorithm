import sys
def input():
    return sys.stdin.readline()

ki,q,l,b,kn,p = map(int,input().strip().split())
print(1-ki, 1-q, 2-l, 2-b, 2-kn, 8-p)