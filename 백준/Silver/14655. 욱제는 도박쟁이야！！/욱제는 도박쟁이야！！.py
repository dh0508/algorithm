import sys
def input():
    return sys.stdin.readline()

N = int(input())
ol = list(map(int,input().strip().split()))
tl = list(map(int,input().strip().split()))
print(sum(map(abs, ol)) + sum(map(abs, ol)))