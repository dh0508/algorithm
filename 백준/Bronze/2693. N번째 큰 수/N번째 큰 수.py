import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for _ in range(test_case):
    l = list(map(int,input().strip().split()))
    l.sort()
    print(l[-3])