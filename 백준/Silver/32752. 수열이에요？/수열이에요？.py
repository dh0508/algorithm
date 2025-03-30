import sys
def input():
    return sys.stdin.readline()

N, L, R = map(int,input().strip().split())
l = list(map(int,input().strip().split()))
ll = l[:L-1] + sorted(l[L-1:R]) + l[R:]

if ll == sorted(l):
    print(1)
else:
    print(0)