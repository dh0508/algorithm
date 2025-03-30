import sys
def input():
    return sys.stdin.readline()

T = int(input())
for _ in range(T):
    a,b = map(int,input().strip().split())
    if a>=b:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")