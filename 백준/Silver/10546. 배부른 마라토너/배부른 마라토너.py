import sys
def input():
    return sys.stdin.readline()

N = int(input())
d = {}
for _ in range(N):
    a = input().strip()
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

for _ in range(N-1):
    a = input().strip()
    d[a] -= 1
for key, value in d.items():
    if value == 1:
        print(key)