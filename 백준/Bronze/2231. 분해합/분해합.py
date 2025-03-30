a = int(input())
b = 0
l = []
for b in range(1, 1000000):
    l.append(b)
for b in l:
    if a == sum(list(map(int,str(b)))) + b:
        print(b)
        break
else:
    print(0)