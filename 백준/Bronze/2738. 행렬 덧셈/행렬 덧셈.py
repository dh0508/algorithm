y,x = map(int,input().split())
a = [input().split()for _ in range(y)]
b = [input().split()for _ in range(y)]
c = [['' for _ in range(x)] for _ in range(y)]
for j in range(x):
    for i in range(y):
        c[i][j] = int(a[i][j]) + int(b[i][j])

for i in range(y):
    print(*c[i])
