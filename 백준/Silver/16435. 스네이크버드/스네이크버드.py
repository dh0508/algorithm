import sys
def input():
    return sys.stdin.readline()

N, L = map(int, input().strip().split())
l = list(map(int,input().strip().split()))
l.sort()
while l:
    a = l.pop(0)
    if L >= a:
        L += 1
    else:
        break
print(L)