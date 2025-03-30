N = int(input())
l = list(map(int,input().strip().split()))
tl = []
cnt = 0
for i in l:
    if i in tl:
        cnt += 1
    else:
        tl.append(i)
print(cnt)