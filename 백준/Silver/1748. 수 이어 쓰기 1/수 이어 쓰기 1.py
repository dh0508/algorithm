import sys
def input():
    return sys.stdin.readline()

n = int(input())
ans = 0
for i in [100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10]:
    if n >= i:
        ans += (n-i+1) * len(str(i))
        n -= ((n//i - 1)*i)
        n -= (n%i)+1
print(ans + n)