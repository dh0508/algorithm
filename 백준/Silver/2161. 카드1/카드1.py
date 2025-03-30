import sys
def input():
    return sys.stdin.readline()

N = int(input())
q = [i for i in range(1,1+N)]
for _ in range(N-1):
    print(q.pop(0), end= ' ')
    q.append(q.pop(0))
print(*q)