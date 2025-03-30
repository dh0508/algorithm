import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for i in range(test_case):
    a, b = map(int,input().split())
    print('Case #',i+1,': ', (a+b), sep='')