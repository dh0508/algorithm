import sys
def input():
    return sys.stdin.readline()

T = int(input())
for _ in range(T):
    N = int(input())
    l = list(map(int, input().strip().split()))
    print(min(l), max(l))