import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = []
for i in range(n):
  a = list(map(int,input().strip().split()))
  l.append(a)

l.sort()

for i in l:
    print(*i)