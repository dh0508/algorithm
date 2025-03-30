a, b = map(int,input().split())
p = 1
for i in range(b):
    p *= a
    a -= 1
for i in range(b):
    p /= b
    b -= 1
print(int(p))