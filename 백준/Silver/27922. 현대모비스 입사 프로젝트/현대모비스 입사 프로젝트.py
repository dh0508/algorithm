import sys
def input():
    return sys.stdin.readline()

N, K = map(int,input().strip().split())
l = [list(map(int,input().strip().split())) for _ in range(N)]
al = [l[i][0] + l[i][1] for i in range(N)]
bl = [l[i][0] + l[i][2] for i in range(N)]
cl = [l[i][2] + l[i][1] for i in range(N)]
al.sort(reverse=True)
bl.sort(reverse=True)
cl.sort(reverse=True)
print(max(sum(al[:K]), sum(bl[:K]), sum(cl[:K])))