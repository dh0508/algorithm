import sys
def input():
    return sys.stdin.readline()

n = int(input())
an = set(map(int,input().strip().split()))
m = int(input())
ml = list(map(int,input().strip().split()))

for i in ml:
    if i in an:
        print(1)
    else:
        print(0)