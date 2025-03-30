import sys
def input():
    return sys.stdin.readline()

s, e = map(int,input().strip().split())

l = [False, False] + [True for _ in range(1000000)]
prime = []
for i in range(len(l)):
    if l[i]:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            l[j] = False

for i in prime:
    if s <= i <= e:
        print(i)