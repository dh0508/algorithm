import sys
def input():
    return sys.stdin.readline()

n, m = map(int, input().split())
pl = []
sl = []
l = []
for _ in range(n):
    p, s = map(int, input().split())
    pl.append(p)
    sl.append(s)
for i in range(n):
    d = []
    for j in range(n):
        if i == j:
            d.append(pl[j] // 2 + sl[j])
        else:
            d.append(pl[j] + sl[j])
    count = 0
    sum = 0
    d.sort()
    for j in range(n):
        sum += d[j]
        if sum > m:
            break
        count += 1
    l.append(count)   

print(max(l))