import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = []
for _ in range(n):
    a = int(input())
    if a == 0:
        l.pop(-1)
    else:
        l.append(a)
print(sum(l))