import sys
def input():
    return sys.stdin.readline()

a=int(input())
s=0
for i in range(1,1+a):
    s += i
print(s)