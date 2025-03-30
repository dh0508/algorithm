import sys
def input():
    return sys.stdin.readline()

n, p = map(int,input().strip().split())
l = []
a = n
while not a in l:
    l.append(a)
    a = a * n % p

print(len(l) - l.index(a))