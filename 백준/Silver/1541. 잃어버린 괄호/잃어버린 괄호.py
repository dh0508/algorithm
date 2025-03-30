import sys
def input():
    return sys.stdin.readline()

l = input().split('-')
p = 0
for i in l[0].split('+'):
    p += int(i)
for i in l[1:]:
    for j in i.split('+'):
        p -= int(j)
print(p)