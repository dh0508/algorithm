n, m = map(int,input().split())
lis = list(map(int, input().split()))
a = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a.append(lis[i] + lis[j] + lis[k])

q = 0
a.sort()

for i in a:
    if i > m:
        print(a[q-1])
        break
    else:
        q += 1

if a[-1] < m:
    print(a[-1])