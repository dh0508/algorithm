import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for _ in range(test_case):
    k = int(input())
    n = int(input())
    l = [[i for i in range(0, 1+n)]]
    for i in range(1 ,k+1):
        l.append([0])
        for j in range(1, 1+n):
            l[i].append(l[i-1][j] + l[i][j-1])

    print(l[-1][-1])