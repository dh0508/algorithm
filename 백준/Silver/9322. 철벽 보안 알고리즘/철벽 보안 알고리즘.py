import sys
def input():
    return sys.stdin.readline()

T = int(input())
for _ in range(T):
    n = int(input())
    l = list(input().strip().split())
    ll = list(input().strip().split())
    pwdl = list(input().strip().split())
    rl = []
    ansl = [0 for _ in range(n)]
    for i in range(n):
        rl.append(l.index(ll[i]))
    for i in range(n):
        ansl[rl[i]] = pwdl[i]
    print(*ansl)