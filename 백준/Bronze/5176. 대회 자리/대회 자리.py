import sys
def input():
    return sys.stdin.readline()

K = int(input())
for _ in range(K):
    P, M = map(int,input().strip().split())
    l = [int(input()) for _ in range(P)]
    ll = []
    p = 0
    for i in l:
        if i in ll:
            p += 1
        else:
            ll.append(i)
    print(p)