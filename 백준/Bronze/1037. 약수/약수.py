import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().strip().split()))
l.sort()
print(l[0] * l[-1])