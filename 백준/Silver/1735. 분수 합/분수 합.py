import sys
def input():
    return sys.stdin.readline()

a1, a2 = map(int, input().strip().split())
b1, b2 = map(int, input().strip().split())
c1 = a1 * b2 + b1 * a2
c2 = a2 * b2
def GCD(x,y):
    while y:
        x, y = y, x%y
    return x

gcd = GCD(c1, c2)
print(int(c1/gcd), int(c2/gcd))