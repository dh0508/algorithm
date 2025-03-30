import sys
def input():
    return sys.stdin.readline().strip()

c = input()[:5]
n = int(input())
l = []
s = 0
for _ in range(n):
    l.append(input())
for i in range(n):
    if c == l[i][:5]:
        s += 1
print(s)