import sys
def input():
    return sys.stdin.readline()

tile_num = 1

def tromino(board, size, top, left, hole_r, hole_c):
    global tile_num
    if size == 2:
        for r in range(2):
            for c in range(2):
                if (top + r, left + c) != (hole_r, hole_c):
                    board[top + r][left + c] = tile_num
        tile_num += 1
        return
    half = size // 2
    mid_r, mid_c = top + half, left + half
    if hole_r < mid_r and hole_c < mid_c:
        quad = 1
    elif hole_r < mid_r and hole_c >= mid_c:
        quad = 2
    elif hole_r >= mid_r and hole_c < mid_c:
        quad = 3
    else:
        quad = 4
    t = tile_num
    tile_num += 1
    if quad != 1: board[mid_r-1][mid_c-1] = t
    if quad != 2: board[mid_r-1][mid_c] = t
    if quad != 3: board[mid_r][mid_c-1] = t
    if quad != 4: board[mid_r][mid_c] = t
    if quad == 1:
        tromino(board, half, top, left, hole_r, hole_c)
    else:
        tromino(board, half, top, left, mid_r-1, mid_c-1)
    if quad == 2:
        tromino(board, half, top, mid_c, hole_r, hole_c)
    else:
        tromino(board, half, top, mid_c, mid_r-1, mid_c)
    if quad == 3:
        tromino(board, half, mid_r, left, hole_r, hole_c)
    else:
        tromino(board, half, mid_r, left, mid_r, mid_c-1)
    if quad == 4:
        tromino(board, half, mid_r, mid_c, hole_r, hole_c)
    else:
        tromino(board, half, mid_r, mid_c, mid_r, mid_c)

def solution(K, x, y):
    global tile_num
    size = 2 ** K
    board = [[0] * size for _ in range(size)]
    hole_r = size - y
    hole_c = x - 1
    board[hole_r][hole_c] = -1
    tile_num = 1
    tromino(board, size, 0, 0, hole_r, hole_c)
    return board

K = int(input())
x, y = map(int, input().split())
board = solution(K, x, y)
for row in board:
    print(' '.join(map(str, row)))
