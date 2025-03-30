import sys
def input():
    return sys.stdin.readline()

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

N = int(input())
lx = []
ly = []
for _ in range(N):
    x, y = map(int, input().strip().split())
    lx.append(x)
    ly.append(y)
total_distance = 0
for i in range(N - 1):
    total_distance += get_distance(lx[i], ly[i], lx[i + 1], ly[i + 1])

max_distance_reduction = 0
for i in range(1, N - 1):
    left = get_distance(lx[i - 1], ly[i - 1], lx[i], ly[i])
    right = get_distance(lx[i], ly[i], lx[i + 1], ly[i + 1])
    all = get_distance(lx[i - 1], ly[i - 1], lx[i + 1], ly[i + 1])
    distance_reduction = left + right - all
    max_distance_reduction = max(max_distance_reduction, distance_reduction)

print(total_distance - max_distance_reduction)