import sys
def input():
    return sys.stdin.readline()

N = int(input())
al = list(map(int,input().strip().split()))
bl = list(map(int,input().strip().split()))

al.sort()
bl.sort(reverse=True)

p = 0
for i in range(N):
    p += al[i]*bl[i]
print(p)