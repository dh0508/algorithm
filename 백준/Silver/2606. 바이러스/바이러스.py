import sys
def input():
    return sys.stdin.readline()

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int,input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False for _ in range(n+1)]
p = 0
def DFS(x):
    global p
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            p += 1
            DFS(i)
DFS(1)
print(p)