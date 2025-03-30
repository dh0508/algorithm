import sys
def input():
    return sys.stdin.readline()
n, m = map(int,input().split())
d = set()
b = set()
for _ in range(n):
    d.add(input().replace('\n',''))
for _ in range(m):
    b.add(input().replace('\n',''))

p = [*d.intersection(b)]
print(len(p))
p.sort()
for i in p:
    print(i)