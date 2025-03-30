a, b = map(int, input().split())
l = []
t_f = True
while t_f:
    for i in range(2, 10000):
        if a % i == 0 and b % i == 0:
            a /= i
            b /= i
            l.append(i)
            break
        elif i > a or i > b:
            t_f = False

p = 1
for i in range(len(l)):
    p *= l[i]
print(p)
print(int(p*a*b))