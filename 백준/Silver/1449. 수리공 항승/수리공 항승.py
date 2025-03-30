import sys
def input():
    return sys.stdin.readline()

N, L = map(int,input().strip().split())
l = list(map(int,input().strip().split()))
l.sort()
p = 0
while l:
    tape_len = l.pop(0) - 0.5 + L
    for i in range(len(l)-1,-1,-1):
        if l[i] <= tape_len:
            l = l[i+1:]
            break
    p+=1
print(p)