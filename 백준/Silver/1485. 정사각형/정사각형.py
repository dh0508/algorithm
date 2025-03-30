import sys
def input():
    return sys.stdin.readline()

T = int(input())
def length(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1/2)
for _ in range(T):
    l = [list(map(int,input().strip().split())) for _ in range(4)]
    l.sort()
    if length(l[0], l[1]) == length(l[0], l[2]) == length(l[1], l[3]) == length(l[2], l[3]) and round(length(l[0], l[3]), 5) == round(length(l[0], l[1]) * (2**(1/2)), 5):
        print(1)

    else:
        print(0)
