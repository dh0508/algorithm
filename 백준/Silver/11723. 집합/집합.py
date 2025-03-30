import sys
def fun(cmd, num='no'):
    global s
    if cmd == 'add':
        try:
            s.add(num)
        except:
            pass
    if cmd == 'remove':
        try:
            s.remove(num)
        except:
            pass
    if cmd == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    if cmd == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    if cmd == 'all':
        s = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    if cmd == 'empty':
        s = set()


n = int(input())
s = set()
for _ in range(n):
    inp = sys.stdin.readline().split()
    if len(inp) == 1:
        fun(inp[0])
    else:
        fun(inp[0], inp[1])