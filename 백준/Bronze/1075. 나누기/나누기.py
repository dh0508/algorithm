import sys
def input():
    return sys.stdin.readline()

N = list(input().strip())
F = int(input())
for i in range(100):
    if i < 10:
        i = '0'+str(i)
    i = list(str(i))
    N.pop()
    N.pop()
    N += i
    if int(''.join(N)) % F == 0:
        print(*i, sep= '')
        break