import sys
def input():
    return sys.stdin.readline()

n = int(input())
name_list = []
date_list = []
for _ in range(n):
    n, d, m, y = input().strip().split()
    name_list.append(n)
    date_list.append(int(y)*10000+int(m)*100+int(d))
print(name_list[date_list.index(max(date_list))])
print(name_list[date_list.index(min(date_list))])