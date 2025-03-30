import sys
def input():
    return sys.stdin.readline()
n = int(input())
l=list(map(int,input().split()))
l.sort(reverse= True)
p = 0
for i in range(1,1+n):
    p += i*l[i-1]
print(p)