import sys
def input():
    return sys.stdin.readline()

a = int(input())
print('long '*(a//4), 'int', sep='')