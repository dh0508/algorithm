import sys
def input():
    return sys.stdin.readline()

N, K = map(int, input().split())
disl = []
for _ in range(N):
    disl.append(list(map(int, input().split())))
coml = list(input())
curx, cury = 0, 0
for com in coml:
    if com == "U":
        if [curx, cury+1] in disl:
            pass
        else:
            cury += 1
    elif com == "D":
        if [curx, cury-1] in disl:
            pass
        else:
            cury -= 1
    elif com == "R":
        if [curx+1, cury] in disl:
            pass
        else:
            curx += 1
    elif com == "L":
        if [curx-1, cury] in disl:
            pass
        else:
            curx -= 1
print(curx, cury)