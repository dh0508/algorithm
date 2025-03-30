import sys
def input():
    return sys.stdin.readline()

def solution(x,y,n):
    global b,w
    c = l[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if l[i][j] != c:
                solution(x, y, n//2)
                solution(x+n//2, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    if c == 1:
        b += 1
    else:
        w += 1
n = int(input())
l = [list(map(int,input().strip().split())) for _ in range(n)]
w = 0
b = 0
solution(0,0, n)
print(w)
print(b)