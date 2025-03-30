lis = []
for i in range(9):
    lis.append(int(input()))

lis =tuple(lis)
print(max(lis))
print(lis.index(max(lis))+1)