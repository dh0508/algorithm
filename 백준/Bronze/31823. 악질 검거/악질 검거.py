import sys
def input():
    return sys.stdin.readline().strip()

n, m = map(int,input().strip().split())
nl = []
l = []
sl = []
for _ in range(n):
    a = input().strip().replace(' ','')
    nl.append(a[m:])
    l.append(a[:m])
for i in range(n):
    r_s = 0
    tmp_r_s = 0
    for j in range(m):
        if l[i][j] == '*':
            tmp_r_s = 0
        else:
            tmp_r_s += 1
        r_s = max(r_s,tmp_r_s)
    sl.append(r_s)
print(len(set(sl)))
for i in range(n):
    print(sl[i], nl[i])