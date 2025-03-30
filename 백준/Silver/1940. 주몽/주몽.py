import sys
def input():
    return sys.stdin.readline()

N = int(input())
M = int(input())
l = list(map(int,input().strip().split()))
l.sort()
p = 0
left = 0
right = N-1
while left < right:
    if l[left] + l[right] > M:
        right -= 1
    elif l[left] + l[right] < M:
        left += 1
    elif l[left] + l[right] == M:
        p += 1
        left += 1
        right -= 1

print(p)