import sys
def input():
    return sys.stdin.readline()

l = []
for _ in range(7):
    a = int(input())
    if a%2 != 0:
        l.append(a)
if l == []:
    print(-1)
else:
    print(sum(l))
    print(min(l))