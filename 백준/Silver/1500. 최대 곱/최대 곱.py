import sys
def input():
    return sys.stdin.readline()

S, K = map(int, input().strip().split())
a = S // K
l = [a for _ in range(K)]
b = S % K
for i in range(b):
    l[i] += 1
p = 1
for i in l:
    p *= i
print(p)