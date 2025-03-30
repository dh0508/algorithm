import sys
def input():
    return sys.stdin.readline()

n, m = map(int,input().split())
d = {}
for i in range(1,1+n):
    d[i] = input().replace('\n','')
dd = {v:k for k,v in d.items()}
for i in range(m):
    inp = input().replace('\n','')
    try:
        inp = int(inp)
    except:
        pass
    if isinstance(inp, int):
        print(d[inp])
    else:
        print(dd[inp])