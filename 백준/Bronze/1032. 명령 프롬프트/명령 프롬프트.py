import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = [input().strip() for _ in range(N)]
p = l[0]
for i in range(N-1):
    a = l[i+1]
    for j in range(len(p)):
        if p[j] != a[j]:
            p = p[:j]+'?'+p[j+1:]
print(p)