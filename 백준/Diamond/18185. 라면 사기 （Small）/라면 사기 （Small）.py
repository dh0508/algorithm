import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = list(map(int,input().strip().split()))
l += [0,0]
m = 0

for i in range(n):
    if l[i+1] > l[i+2]:
        count = min(l[i], l[i+1] - l[i+2])
        l[i] -= count
        l[i+1] -= count
        m += count * 5

        count = min(l[i], l[i+1], l[i+2])
        l[i] -= count
        l[i+1] -= count
        l[i+2] -= count
        m += count * 7

    else:
        count = min(l[i], l[i + 1], l[i + 2])
        l[i] -= count
        l[i + 1] -= count
        l[i + 2] -= count
        m += count * 7

        count = min(l[i], l[i+1])
        l[i] -= count
        l[i + 1] -= count
        m += count * 5

    m += l[i] * 3
print(m)