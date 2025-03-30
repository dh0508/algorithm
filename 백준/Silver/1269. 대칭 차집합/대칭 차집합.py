import sys
def input():
    return sys.stdin.readline()

An, Bn = map(int,input().strip().split())
a = set(map(int,input().strip().split()))
b = set(map(int,input().strip().split()))
print(len(a-b)+len(b-a))