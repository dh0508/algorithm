import sys
def input():
    return sys.stdin.readline()

print(*sorted(list(map(int,input().strip().split()))))