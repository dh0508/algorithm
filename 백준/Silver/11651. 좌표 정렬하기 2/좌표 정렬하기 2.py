import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().strip().split())))
l.sort(key= lambda x : (x[1], x[0]))
for i in l:
    print(*i)