import sys
def input():
    return sys.stdin.readline()

N = int(input())
A, B, C = map(int,input().strip().split())
p = 0
for i in [A, B, C]:
    if i > N:
        p += N
    else:
        p += i
print(p)