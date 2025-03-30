import sys
def input():
    return sys.stdin.readline()

n = int(input())
c = 0
six_count = 0
while True:
    c += 1
    if '666' in str(c):
        six_count += 1
    if six_count == n:
        print(c)
        break