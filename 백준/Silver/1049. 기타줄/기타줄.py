import sys
def input():
    return sys.stdin.readline()

N, M = map(int,input().strip().split())
package_price = float("inf")
one_price = float("inf")
for _ in range(M):
    p, o = map(int,input().strip().split())
    package_price = min(p,package_price)
    one_price = min(o,one_price)
print(min(((N//6)*package_price + (N%6)*one_price), ((N//6+1)*package_price), N*one_price))