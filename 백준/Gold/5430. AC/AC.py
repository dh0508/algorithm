import sys
from collections import deque


def input():
    return sys.stdin.readline()


def function(l, fun):
    is_reversed = False
    for i in fun:
        if i == 'D':
            if not l:
                print('error')
                return
            if is_reversed:
                l.pop()
            else:
                l.popleft()
        else:
            is_reversed = not is_reversed

    if is_reversed:
        l.reverse()

    print('[' + ','.join(map(str, l)) + ']')


test_case = int(input())
for _ in range(test_case):
    fun = list(input().strip())
    n = int(input())
    l = input().strip().replace('[', '').replace(']', '')
    if n == 0:
        l = deque()
    else:
        l = deque(map(int, l.split(',')))
    function(l, fun)
