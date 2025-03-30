import sys
def input():
    return sys.stdin.readline()

a = int(input())
l = [0 for _ in range((1+a)*3)]
l[1]=0
for i in range(1,a+1):
    if l[i*2] == 0 or l[i*2] > l[i]+1:
        l[i*2]=l[i]+1
    if l[i*3] == 0 or l[i*3] > l[i]+1:
        l[i*3]=l[i]+1
    if l[i+1] == 0 or l[i+1] > l[i] + 1:
        l[i+1] = l[i] + 1

print(l[a])