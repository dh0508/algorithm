import sys
def input():
    return sys.stdin.readline()

while True:
    s = input().strip()
    if s == "END":
        break
    s=list(s)
    s.reverse()
    print(''.join(s))