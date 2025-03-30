import sys
def input():
    return sys.stdin.readline()
import math

n = int(input())
l = list(map(int,input().strip().split()))
count = 0
countl = [0] * n
for i in range(1,n):
    p = math.ceil(math.log2((l[i-1]/l[i]))) + countl[i-1]
    if p > 0:
        countl[i] = p
        count += countl[i]
print(count)