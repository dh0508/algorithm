import sys
input = sys.stdin.readline

n = int(input())
l = [''for _ in range(2000001)]
for i in range(n):
    a = int(input())
    l[a+1000000] = 1
for i in range(len(l)):
    if l[i] == 1:
        print(i-1000000)