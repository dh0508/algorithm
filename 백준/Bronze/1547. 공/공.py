import sys
def input():
    return sys.stdin.readline()

ball = 1
N = int(input())
for _ in range(N):
    a, b = map(int,input().strip().split())
    if a == ball:
        ball = b
    elif b == ball:
        ball = a
print(ball)