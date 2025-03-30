import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for _ in range(test_case):
    num = list(input().strip())
    for i in range(1, len(num)):
        if int(num[-i]) >= 5:
            num[-(i+1)] = int(num[-(i+1)])+1
            num[-i] = 0
        else:
            num[-i] = 0
    print(*num,sep='')