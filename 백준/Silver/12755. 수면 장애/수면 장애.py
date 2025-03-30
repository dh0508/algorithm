import sys
def input():
    return sys.stdin.readline()

n = int(input())
a = 0
while n > 0:
    a += 1
    n -= len(str(a))
print(str(a)[-(abs(n)+1)])