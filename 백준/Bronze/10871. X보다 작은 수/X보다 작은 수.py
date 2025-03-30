n, x = map(int, input().split())
num = list(map(int, input().split()))
real_num = []
for i in range(n):
    if num[i] < x:
        real_num.append(num[i])
    else:
        continue
print(*real_num)