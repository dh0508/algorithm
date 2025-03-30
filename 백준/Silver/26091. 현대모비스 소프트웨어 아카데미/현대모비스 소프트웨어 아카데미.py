import sys
def input():
    return sys.stdin.readline()

n, m = map(int, input().strip().split())
ml = list(map(int, input().strip().split()))
ml.sort()
result = 0
one = 0
two = len(ml) - 1

while True:
    if one >= two:
        break

    sum_m = ml[one] + ml[two]
    if sum_m < m:
        one += 1
    else:
        result += 1
        one += 1
        two -= 1
print(result)
