import sys
def input():
    return sys.stdin.readline()

n, x = map(int,input().strip().split())
floor_weight_list = list(map(int,input().strip().split()))
plus_weight_list = list(map(int,input().strip().split()))
die = 0
sum_plus_weight = 0
for i in range(n):
    sum_plus_weight += plus_weight_list[i]
    if sum_plus_weight < floor_weight_list[i]:
        die = 1
        break

if die == 1:
    print(-1)
else:
    print((sum_plus_weight - floor_weight_list[-1]) // x)