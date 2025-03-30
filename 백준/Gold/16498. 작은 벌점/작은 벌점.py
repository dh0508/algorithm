import sys
def input():
    return sys.stdin.readline()

A, B, C  = map(int, input().split())
la = list(map(int, input().split()))
lb = list(map(int, input().split()))
lc = list(map(int, input().split()))
la.sort()
lb.sort()
lc.sort()

p = float("inf")
for i in range(A):

    s, e = 0, B-1
    j = lb[0]
    target = la[i]
    while s <= e:
        m = (s + e) // 2
        if abs(lb[m] - target) < abs(j - target):
            j = lb[m]

        if lb[m] == target:
            j = lb[m]
            break
        elif lb[m] > target:
            e = m - 1
        else:
            s = m + 1


    s, e = 0, C-1
    k = lc[0]
    target = la[i]
    while s <= e:
        m = (s + e) // 2
        if abs(lc[m] - target) < abs(k - target) and abs(lc[m] - j) < abs(k - j):
            k = lc[m]

        if lc[m] == target:
            k = lc[m]
        elif lc[m] > target:
            e = m - 1
        else:
            s = m + 1

    p = min(p, abs(max(la[i], j, k) - min(la[i], j, k)))

print(p)