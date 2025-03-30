l =[]
for _ in range(5):
    a=int(input())
    if a<40:
        a=40
    l.append(a)
print(int(sum(l)//5))