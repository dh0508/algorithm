import sys
def input():
    return sys.stdin.readline()

n = int(input())
s = set()
cnt = 0
for _ in range(n):
    a = input().strip()
    if a == "ENTER":
        s = set()
    else:
        if a not in s:
            s.add(a)
            cnt += 1
print(cnt)