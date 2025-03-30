import sys
def input():
    return sys.stdin.readline()

N, M, V = map(int,input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort()

def DFS(graph, V):
    global visited
    for i in graph[V]:
        if i not in visited:
            visited.append(i)
            DFS(graph, i)

def BFS(graph, V):
    global visited
    queue = [V]
    while queue:
        a = queue.pop(0)
        for i in graph[a]:
            if i not in visited:
                queue.append(i)
                visited.append(i)


visited = [V]
DFS(graph, V)
print(*visited)
visited = [V]
BFS(graph, V)
print(*visited)