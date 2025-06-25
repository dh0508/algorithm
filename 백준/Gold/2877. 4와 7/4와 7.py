import sys
def input():
    return sys.stdin.readline()

K = int(input())
i=1
while K - 2**i > 0:
    K -= 2**i
    i += 1
p = str(bin(K-1))[2:].replace('1', '7').replace('0', '4')
print(p.rjust(i, '4'))