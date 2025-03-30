import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())
ans = 1
for i in range(1, 1+N):
    ans *= i
    ans = str(ans)
    for j in range(len(ans)-1, -1, -1):
        if ans[j] != '0':
            ans = ans[:j+1][-10:]
            break
    ans = int(ans)
print(str(ans)[-1])
