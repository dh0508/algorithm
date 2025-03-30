import sys
def input():
    return sys.stdin.readline()

n = int(input())
x= 0
y = 0
e = 0
for i in range(n):
    a,b = map(int, input().strip().split())
    e += a * y + b * x
    x += a
    y += b
print(e)