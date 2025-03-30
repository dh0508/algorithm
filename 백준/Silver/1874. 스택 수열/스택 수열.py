import sys
def input():
    return sys.stdin.readline()

n = int(input())
il = []
l = [1]
pl = ['+']
count = 1
bug = 0
for _ in range(n):
    il.append(int(input()))

while count != n or len(l) != 0:
    if count > n+1:
        print('NO')
        bug = 1
        break
    if l == []:
        count += 1
        l.append(count)
        pl.append('+')
    else:
        if il[0] == l [-1]:
            pl.append('-')
            l.pop(-1)
            il.pop(0)
        else:
            count += 1
            l.append(count)
            pl.append('+')
if bug == 0:
    print(*pl, sep='\n')