import sys
def input():
    return sys.stdin.readline()

n, k = map(int, input().strip().split())
p = []
l = [i for i in range(1, n + 1)]

index = 0
while l:
    index = (index + k - 1) % len(l)
    p.append(l.pop(index))

print(str(p).replace('[', '<').replace(']', '>'))