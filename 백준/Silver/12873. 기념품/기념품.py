import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = [i for i in range(1,1+N)]
bj = 0
stage = 1
while len(l) != 1:
    d = (pow(stage,3)+bj) % len(l) - 1
    l.pop(d)
    if d == -1:
        bj = 0
    else:
        bj = d
    stage += 1
print(l[0])