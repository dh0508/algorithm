import sys
def input():
    return sys.stdin.readline()

l = list(input().strip())
l.sort(reverse=True)
print(*l, sep='')