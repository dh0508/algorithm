import sys
def input():
    return sys.stdin.readline()

num = list(map(int,input().strip().split()))
alp = list(input().strip())
num.sort()
d = {"A":num[0], "B":num[1], "C":num[2]}
for i in alp:
    print(d[i], end=' ')