import sys
def input():
    return sys.stdin.readline()

def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))
c = list(map(int,input().strip().split()))
d = list(map(int,input().strip().split()))

ab = get_distance(a[0],a[1],b[0],b[1])
ac = get_distance(a[0],a[1],c[0],c[1])
ad = get_distance(a[0],a[1],d[0],d[1])
bc = get_distance(b[0],b[1],c[0],c[1])
bd = get_distance(b[0],b[1],d[0],d[1])
cd = get_distance(c[0],c[1],d[0],d[1])

print(int(min(
    ab+bc+cd,
    ab+bd+cd,
    ac+bc+bd,
    ac+cd+bd,
    ad+bd+bc,
    ad+cd+bc
)))