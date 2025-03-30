import sys
def input():
    return sys.stdin.readline()

def ps_dis(a, b, c):
    dis = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dis += 1
        if b[i] != c[i]:
            dis += 1
        if a[i] != c[i]:
            dis += 1
    return dis

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    l = list(input().strip().split())
    if n > 32:
        print(0)
    else:
        md = 15
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    d = (ps_dis(l[i],l[j],l[k]))
                    if d < md:
                        md = d
        print(md)