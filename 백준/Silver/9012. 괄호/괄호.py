import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for _ in range(test_case):
    inp = input().strip()
    while '()' in inp:
        inp  = inp.replace('()', '')
    if inp == '':
        print('YES')
    else:
        print('NO')