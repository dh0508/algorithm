import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int, input().strip().split()))
# l.sort()


tmp = [[l.pop(0)]]
while l:
    if tmp[-1][-1]*2 in l:
        tmp[-1].append(l.pop(l.index(tmp[-1][-1]*2)))
    elif tmp[-1][-1]%3==0 and tmp[-1][-1]//3 in l:
        tmp[-1].append(l.pop(l.index(tmp[-1][-1]//3)))
    else:
        tmp.append([l.pop(0)])

ans = tmp.pop(0)
while len(ans) != N:
    for i in range(len(tmp)):
        if ans[-1] * 2 == tmp[i][0] or (ans[-1] % 3 == 0 and ans[-1]//3 == tmp[i][0]):
            ans += tmp.pop(i)
            break
        if tmp[i][-1] * 2 == ans[0] or (tmp[i][-1] % 3 == 0 and tmp[i][-1]// 3 == ans[0]):
            ans = tmp.pop(i) + ans
            break
print(*ans)