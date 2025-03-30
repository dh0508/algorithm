import sys
def input():
    return sys.stdin.readline()

n, m = map(int, input().strip().split())
l = list(map(int, input().strip().split()))
s, e = 0, max(l)
while s<=e:
    h = (s+e)//2
    w = []
    for i in l:
        if i > h:
            w.append(i-h)
    if sum(w) >= m:
        s = h+1
    else:
        e = h-1
print(s-1)