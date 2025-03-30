import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = [int(input()) for _ in range(N)]
l.sort()
ll = []
for i in range(N):
    ll.append(l.pop(0) * (N-i))
print(max(ll))