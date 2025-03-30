import sys
def input():
    return sys.stdin.readline()

N = int(input())
print(sum([i for i in range(1,1+N)]))
print(sum([i for i in range(1,1+N)])**2)
print(sum([i**3 for i in range(1,1+N)]))