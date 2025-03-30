import sys
def input():
    return sys.stdin.readline().strip()

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    d = {}
    for _ in range(n):
        name, type = input().strip().split()
        if type in d:
            d[type] += 1
        else:
            d[type] = 1
    value = 1
    for i in d:
        value *= d[i]+1
    print(value-1)