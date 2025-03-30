import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = list(map(int,input().strip().split()))
k = int(input())
count = 0
f = 0
sum = 0

for s in range(n):
    sum += l[s]
    while sum > k and f <= s:
        count += (n-s)
        sum -= l[f]
        f += 1

print(count)