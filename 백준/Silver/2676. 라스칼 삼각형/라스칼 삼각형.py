import sys
def input():
    return sys.stdin.readline()

T = int(input())
for _ in range(T):
    n, m = map(int,input().strip().split())
    print(1+(n-m)*m)
    