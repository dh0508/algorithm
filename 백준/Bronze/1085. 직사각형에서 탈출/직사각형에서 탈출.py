import sys
def input():
    return sys.stdin.readline()

x,y,w,h = map(int, input().strip().split())
print(min(x, abs(x-w), y, abs(y-h)))