import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for _ in range(test_case):
    l = list(input().strip().split())
    ll = []
    for i in l:
        ll.append(i[::-1])
    print(*ll)