import sys
def input():
    return sys.stdin.readline()

a = int(input())
l = []
for _ in range(9):
    l.append(int(input()))
print(a - sum(l))