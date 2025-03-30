import sys
def input():
    return sys.stdin.readline()

l = [int(input()) for _ in range(int(input()))]
l.append(0)
d = l.pop(0)
cnt = 0
while max(l) >= d:
    l[l.index(max(l))] -= 1
    d += 1
    cnt += 1
print(cnt)