import sys
def input():
    return sys.stdin.readline()

def dfs(n, depth, product, results):
    if depth == n:
        results.add(product)
        return
    for i in range(1, 10):
        dfs(n, depth + 1, product * i, results)

n = int(input())
results = set()
dfs(n, 0, 1, results)
print(len(results))