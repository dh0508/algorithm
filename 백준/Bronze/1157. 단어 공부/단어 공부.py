a = (input().upper())
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1

if list(b.values()).count(max(b.values())) > 1:
    print('?')
else:
    c = {v: k for k, v in b.items()}

    print(c[max(c)])
