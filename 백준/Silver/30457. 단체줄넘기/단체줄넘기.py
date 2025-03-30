import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().strip().split()))
l.sort()
p = 1
ll = [l[0]]
for i in range(1, N):
    if l[i]>l[i-1]:
        p += 1
        ll.append(l[i])

lll = []
for i in range(N):
    if l[i] in ll:
        ll.pop(ll.index(l[i]))
    else:
        lll.append(l[i])

if lll:
    p += 1
    for i in range(1, len(lll)):
        if lll[i]>lll[i-1]:
            p += 1

print(p)