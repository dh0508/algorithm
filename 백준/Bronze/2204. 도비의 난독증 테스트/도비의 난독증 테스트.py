import sys
def input():
    return sys.stdin.readline()

while True:
    n = int(input())
    if n != 0:
        l = []
        d = {}
        for _ in range(n):
            a = input().strip()
            d[a.lower()] = a
            l.append(a.lower())
        l.sort()
        print(d[l[0]])
    else:
        exit()