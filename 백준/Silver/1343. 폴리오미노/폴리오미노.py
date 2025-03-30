import sys
def input():
    return sys.stdin.readline()

def solution():
    l = list(input().strip().split('.'))
    for i in range(len(l)):
        if len(l[i]) % 2 == 1:
            print(-1)
            return
        else:
            if len(l[i]) % 4 == 0:
                l[i] = 'A' * len(l[i])
            else:
                l[i] = 'A' * (len(l[i])-2) + 'B' * 2
    print('.'.join(l))
solution()