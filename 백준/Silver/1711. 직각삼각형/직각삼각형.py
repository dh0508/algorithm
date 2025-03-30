import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = []
for _ in range(N):
    l.append(list(map(int,input().strip().split())))
p = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            a, b, c = l[i], l[j], l[k]
            A = ((c[0]-b[0])**2 + (c[1]-b[1])**2)
            B = ((c[0]-a[0])**2 + (c[1]-a[1])**2)
            C = ((a[0]-b[0])**2 + (a[1]-b[1])**2)
            if 2 * max(A,B,C) == A + B + C:
                p += 1
print(p)