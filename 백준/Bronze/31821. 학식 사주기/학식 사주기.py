import sys
def input():
    return sys.stdin.readline().strip()

n = int(input())
a = {}
for i in range(1,1+n):
    a[i] = int(input())
m = int(input())
b = []
for _ in range(m):
    b.append(int(input()))
sum = 0
for i in range(m):
    sum += a[b[i]]
print(sum)