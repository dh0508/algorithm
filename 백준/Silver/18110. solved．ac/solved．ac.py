import sys
def input():
    return sys.stdin.readline()

def round(a):
  if a - int(a) >= 0.5:
    return int(a)+1
  else:
    return int(a)

n = int(input())
if n == 0:
    print(0)
else:
    l = []
    for _ in range(n):
        l.append(int(input()))
    l.sort()
    mp = round(n*15/100)
    if mp > 0:
        l = l[mp:-mp]
    print(round(sum(l)/len(l)))