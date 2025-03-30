import sys
def input():
    return sys.stdin.readline()

s_y, s_m, s_d = map(int, input().strip().split())
e_y, e_m, e_d = map(int, input().strip().split())
y = 0
m = 0
d = (e_y*360 + e_m*30 + e_d)-(s_y*360 + s_m*30 + s_d)
if d//30 >= 36:
    m = 36
else:
    m = d//30

for i in range(d//360):
    y += i // 2 + 15


print(y, m)
print((360*(e_y - s_y) + 30*(e_m-s_m) + e_d-s_d),'days',sep= '')