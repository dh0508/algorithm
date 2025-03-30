import sys
def input():
    return sys.stdin.readline()

l=[[] for _ in range(50)]
n = int(input())
for _ in range(n):
    a = input().strip()
    l[len(a)-1].append(a)
for i in range(len(l)):
    if l[i] == []:
        pass
    else:
        l[i] = list(set(l[i]))
        l[i].sort()
        for j in range(len(l[i])):
            print(l[i][j])