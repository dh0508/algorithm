import sys
def input():
    return sys.stdin.readline()

N = int(input())
if N == 1:
    print(5)
else:
    p = 5
    s = 7
    for _ in range(N-1):
        p += s
        s += 3
    print(p%45678)