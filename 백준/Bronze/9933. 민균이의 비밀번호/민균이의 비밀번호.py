import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = []
for _ in range(n):
    l.append(input().strip())
for i in l:
    if i[::-1] in l:
        print(len(i), i[len(i)//2])
        break