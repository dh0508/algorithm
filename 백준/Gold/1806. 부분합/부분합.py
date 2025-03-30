import sys
def input():
    return sys.stdin.readline()

N, S = map(int,input().strip().split())
l = list(map(int,input().strip().split()))

left = -1
right = -1
value = 0
ans = 100001

while left <= right and right < len(l):
    if value >= S:
        ans = min(ans, right - left)
        left += 1
        try:
            value -= l[left]
        except:
            break
    else:
        right += 1
        try:
            value += l[right]
        except:
            break

if ans == 100001:
    print(0)
else:
    print(ans)