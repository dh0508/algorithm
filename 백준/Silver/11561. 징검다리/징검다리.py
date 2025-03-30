import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    count = 0
    start = 0
    end = 150000000
    while start < end:
        mid = (start+end)//2
        if mid*(mid+1)//2 <= n:
            count = mid
            start = mid+1
        else:
            end = mid
    print(count)