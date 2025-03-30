import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = [[] for _ in range(201)]
for _ in range(n):
    age, name = input().strip().split()
    l[int(age)].append(name)
for i in l:
    if i == []:
        pass
    else:
        for j in i:
            print(l.index(i), j)