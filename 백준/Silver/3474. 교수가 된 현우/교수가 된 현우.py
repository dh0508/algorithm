import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    count = 0
    while n >= 5:
        n //= 5
        count += n
    print(count)