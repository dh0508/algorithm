import sys
def input():
    return sys.stdin.readline()

a = input().strip()
N = int(input())
l = [input().strip() for _ in range(N)]
cnt = 0
for i in range(N):
    aa = l[i]
    for _ in range(len(a)):
        aa = list(aa)
        aa.append(aa.pop(0))
        aa = "".join(aa)
        if a in aa:
            cnt += 1
            break
print(cnt)