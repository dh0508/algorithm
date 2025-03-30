import sys
def input():
    return sys.stdin.readline()
n, m = map(int,input().split())
dic={}
for _ in range(n):
    site, passwd = input().split()
    dic[site] = passwd
for _ in range(m):
    print(dic[input().replace('\n', '')])