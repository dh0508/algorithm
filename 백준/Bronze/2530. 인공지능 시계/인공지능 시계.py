import sys
def input():
    return sys.stdin.readline()

h, m, s = map(int,input().strip().split())
ps = int(input())
s += ps
if s >= 60:
    m += s // 60
    s %= 60
if m >= 60:
    h += m // 60
    m %= 60
h %= 24
print(h, m, s)