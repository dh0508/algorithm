import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().strip().split()))
maxdp = l
mindp = l
for _ in range(N-1):
    l = list(map(int,input().strip().split()))
    maxdp = [l[0] + max(maxdp[0], maxdp[1]), l[1] + max(maxdp), l[2] + max(maxdp[1], maxdp[2])]
    mindp = [l[0] + min(mindp[0], mindp[1]), l[1] + min(mindp), l[2] + min(mindp[1], mindp[2])]
print(max(maxdp), min(mindp))