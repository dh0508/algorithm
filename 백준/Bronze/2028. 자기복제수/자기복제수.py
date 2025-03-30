import sys
def input():
    return sys.stdin.readline()

T = int(input())
for _ in range(T):
    N = int(input())
    if str(N) == str(N**2)[-len(str(N)):]:
        print("YES")
    else:
        print("NO")