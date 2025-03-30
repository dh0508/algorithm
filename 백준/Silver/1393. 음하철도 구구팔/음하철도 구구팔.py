import sys
def input():
    return sys.stdin.readline()
import math

xs, ys = map(int,input().strip().split())
xe, ye, dx, dy = map(int,input().strip().split())
dxdy = math.gcd(dx,dy)
dx //= dxdy
dy //= dxdy
r = abs(xs-xe)**2 + abs(ys-ye)**2
while True:
    xe += dx
    ye += dy
    if abs(xs-xe)**2 + abs(ys-ye)**2 > r:
        print(xe-dx, ye-dy)
        break
    r = abs(xs - xe) ** 2 + abs(ys - ye) ** 2