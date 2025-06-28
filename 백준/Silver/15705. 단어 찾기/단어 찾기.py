import sys
def input():
    return sys.stdin.readline()

S = input().strip()
N, M = map(int, input().strip().split())
board = [input().strip() for _ in range(N)]

dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

ans = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == S[0]:
            for dx, dy in dxdy:
                x, y = i, j
                right = True
                for k in range(len(S)):
                    if 0 <= x < N and 0 <= y < M and board[x][y] == S[k]:
                        x += dx
                        y += dy
                    else:
                        right = False
                        break
                if right:
                    ans = 1
                    break
        if ans:
            break
    if ans:
        break

print(ans)