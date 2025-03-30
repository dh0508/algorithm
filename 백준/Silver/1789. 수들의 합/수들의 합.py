import sys
def input():
    return sys.stdin.readline()

N = int(input())
value = 0
cnt = 0
while value <= N:
    cnt += 1
    value += cnt
print(cnt-1)