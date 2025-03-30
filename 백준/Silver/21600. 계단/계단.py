import sys
def input():
    return sys.stdin.readline()

n = int(input())
h = list(map(int,input().strip().split()))
stair_list = []
stair = 1
for i in range(n):
    if stair <= h[i]:
        stair += 1
    else:
        stair_list.append(stair-1)
        stair = h[i] +1
stair_list.append(stair-1)
print(max(stair_list))