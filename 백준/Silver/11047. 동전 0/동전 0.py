import sys
def input():
    return sys.stdin.readline()
l = []
c = 0
n, k = map(int,input().split())
for i in range(n):
    l.append(int(input()))
l = l[::-1]
while k != 0:
    for i in l:
        if k % i == k:
            pass
        else:
            c += (k//i)
            k %= i
print(c)