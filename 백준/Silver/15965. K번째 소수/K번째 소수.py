import sys
def input():
    return sys.stdin.readline()

k = int(input())
high = 10**7
l = [True] * (high+1)
p_m = []
for i in range(2,int(high+1)):
    if l[i]:
        p_m.append(i)
        for j in range(i*i, high+1, i):
            l[j] = False
print(p_m[k-1])