import sys
def input():
    return sys.stdin.readline()

n, m = map(int,input().split())
n_l = list(map(int, input().split()))
n_s_l = [0 for _ in range(n+1)]
n_s_l[1] = n_l[0]
for i in range(2,n+1):
    n_s_l[i] = n_s_l[i-1] + n_l[i-1]
for _ in range(m):
    i, j = map(int,input().split())
    print(n_s_l[j]-n_s_l[i-1])