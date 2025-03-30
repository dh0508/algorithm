import sys
def input():
    return sys.stdin.readline()

N = int(input())
for _ in range(N):
    c, p = map(int, input().strip().split())
    print(c, p)
    print(c*p - 2*(c-1))