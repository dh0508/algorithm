import sys
def input():
    return sys.stdin.readline()

T = int(input())
def distance(x1, y1, x2, y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**(1/2)
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().strip().split())
    d = distance(x1, y1, x2, y2)
    if r1 > r2:
        bc = [x1, y1, r1]
        sc = [x2, y2, r2]
    else:
        sc = [x1, y1, r1]
        bc = [x2, y2, r2]

    if x1 == x2 and y1== y2 and r1 == r2:
        print(-1)
    elif r1 + r2 == d or bc[2] == sc[2] + d:
        print(1)
    elif r1 + r2 < d or bc[2] > sc[2] + d:
        print(0)
    else:
        print(2)