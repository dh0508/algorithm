import sys
def input():
    return sys.stdin.readline()

n , m = map(int, input().strip().split())
l = []
p = []
for _ in range(n):
    l.append(input().strip())

for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0
        for ii in range(i, i+8):
            for jj in range(j, j+8):
                if (ii + jj)%2 == 0:
                    if l[ii][jj] != 'B':
                        w += 1
                    if l[ii][jj] != 'W':
                        b += 1
                else:
                    if l[ii][jj] != 'W':
                        w += 1
                    if l[ii][jj] != 'B':
                        b += 1
        p.append(w)
        p.append(b)
print(min(p))