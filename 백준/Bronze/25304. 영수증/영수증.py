import sys
def input():
    return sys.stdin.readline()

a = int(input())
n = int(input())
s = []
for _ in range(n):
    b,c = map(int,input().split())
    s.append(b*c)
if sum(s) == a:
    print('Yes')
else:
    print('No')