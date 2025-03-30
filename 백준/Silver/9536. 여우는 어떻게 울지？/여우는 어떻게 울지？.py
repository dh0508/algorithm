import sys
def input():
    return sys.stdin.readline()

for _ in range(int(input())):
    l = list(input().strip().split())
    ll = []
    while True:
        a = input().strip()
        if a != "what does the fox say?":
            aa = list(a.split())
            ll.append(aa[-1])
        else:
            break
    for i in range(len(l)):
        if l[i] in ll:
            pass
        else:
            print(l[i], end=" ")