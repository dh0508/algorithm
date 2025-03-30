import sys
def input():
    return sys.stdin.readline()

n = int(input().strip())
m = int(input().strip())
a = 1
b = 1
for i in range(n-1):
    a *= m-1-i
    b *= i+1
print(int(a/b))