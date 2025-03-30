import sys
def input():
    return sys.stdin.readline()

for _ in range(3):
    N = int(input())
    value = 0
    for _ in range(N):
        value += int(input())
    if value == 0:
        print(0)
    elif value > 0:
        print("+")
    else:
        print("-")