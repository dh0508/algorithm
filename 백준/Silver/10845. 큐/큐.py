import sys
def input():
    return sys.stdin.readline()

def solution(cmd, num = 'x'):
    if cmd == 'push':
        l.append(num)
    if cmd == 'pop':
        try:
            print(l.pop(0))
        except:
            print(-1)
    if cmd == 'size':
        print(len(l))
    if cmd == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)
    if cmd == 'back':
        try:
            print(l[-1])
        except:
            print(-1)
    if cmd == 'front':
        try:
            print(l[0])
        except:
            print(-1)
n = int(input())
l = []
for _ in range(n):
    i = input().strip()
    try:
        cmd, num = i.split()
        solution(cmd, num)
    except:
        solution(i)