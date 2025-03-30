import sys
def input():
    return sys.stdin.readline()

A, B, D = map(int,input().strip().split())
l = [1 for _ in range(B+1)]
for i in range(2, int(B**(1/2))+1):
    if not l[i]:
        continue
    for j in range(i*i, B+1, i):
        l[j] = False
cnt = 0
for i in range(A, B+1):
    if l[i]:
        if str(D) in str(i):
            cnt += 1
print(cnt)