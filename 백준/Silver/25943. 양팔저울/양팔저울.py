import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = list(map(int,input().strip().split()))
left, right = l[0], l[1]
for i in range(2,n):
    if left > right:
        right += l[i]
    elif left <= right:
        left += l[i]
dif = abs(left - right)
cnt = 0
for i in [100, 50, 20, 10, 5, 2, 1]:
    cnt += dif//i
    dif %= i
print(cnt)