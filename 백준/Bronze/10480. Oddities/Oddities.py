import sys
def input():
    return sys.stdin.readline()


T = int(input())
for _ in range(T):
    a = int(input())
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")