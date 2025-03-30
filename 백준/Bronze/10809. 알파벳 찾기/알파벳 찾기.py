s = list(input())
alp = list('abcdefghijklmnopqrstuvwxyz')
pl = []
for i in alp:
    if i in s:
        pl.append(s.index(i))
    else:
        pl.append(-1)
print(*pl)