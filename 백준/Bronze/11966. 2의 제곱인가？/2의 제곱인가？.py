import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = []
for i in range(0,31):
    l.append(2**i)
if N in l:
    print(1)
else:
    print(0)