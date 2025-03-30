import sys
def input():
    return sys.stdin.readline()

r, c = map(int, input().strip().split())
m = []
for _ in range(r):
    m.append(list(input().strip()))
nm = [arr[:] for arr in m]

for y in range(r):
    for x in range(c):
        if m[y][x] =='X':
            o = 0
            if y == 0 or m[y - 1][x] == '.':
                o += 1
            if y == r - 1 or m[y + 1][x] == '.':
                o += 1
            if x == 0 or m[y][x - 1] == '.':
                o += 1
            if x == c - 1 or m[y][x + 1] == '.':
                o += 1

            if o >= 3:
                nm[y][x] = '.'

max_x = 0
min_x = c
max_y = 0
min_y = r
for y in range(r):
    for x in range(c):
        if nm[y][x] == 'X':
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y

nm = nm[min_y:max_y + 1]
for i in nm:
    print(*i[min_x:max_x + 1], sep='')