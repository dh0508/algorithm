import sys
def input():
    return sys.stdin.readline()

N, M, a, K = map(int, input().strip().split())
l_o_t = a - K
import math
if l_o_t < N:
    print(l_o_t+1,end=' ')
else:
    print(N,end=' ')
print(math.ceil(l_o_t/M)+1)