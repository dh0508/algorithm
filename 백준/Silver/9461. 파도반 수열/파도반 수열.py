import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    l = [0 for _ in range(n+6)]
    l[1]=1
    l[2]=1
    l[3]=1
    l[4]=2
    l[5]=2
    for i in range(5,n+1):
        l[i] = l[i-1]+l[i-5]
    print(l[n])