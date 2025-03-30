import sys
def input():
    return sys.stdin.readline()

def solution():
    m, n, x, y = map(int,input().strip().split())
    a = x
    while a <= m*n:
        if (a-x) % m == 0 and (a-y) % n == 0:
            print(a)
            return
        a += m
    print(-1)
    return

test_case = int(input())
for _ in range(test_case):
    solution()