import sys
def input():
    return sys.stdin.readline()

n, m = map(int,input().split())
l = [i for i in range(0, 1+n)]
for _ in range(m):
    i, j = map(int, input().split())
    cl = l[i:j+1]
    l = l[0:i]+cl[::-1]+l[j+1:]
print(*l[1:])