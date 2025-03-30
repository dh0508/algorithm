import sys
def input():
    return sys.stdin.readline()

G = int(input())
curr = 2
prev = 1
tf = False
while prev < curr:
    if curr**2 - prev**2 == G:
        print(curr)
        curr += 1
        tf = True
    elif curr**2 - prev**2 > G:
        prev += 1
    else:
        curr += 1
if not tf:
    print(-1)