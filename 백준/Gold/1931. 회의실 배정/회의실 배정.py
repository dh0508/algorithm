import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = []
count = 0
for _ in range(n):
    l.append(list(map(int,input().strip().split())))
l.sort(key=lambda x: (x[1],x[0]))
le = 0
for s, pe in l:
    if s >= le:
        count += 1
        le = pe
print(count)