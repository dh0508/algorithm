import sys
def input():
    return sys.stdin.readline()

n = int(input())
log_dic = {}
l = []
for _ in range(n):
    name, el = input().strip().split()
    log_dic[name] = el
for i in log_dic:
    if log_dic[i] == 'enter':
        l.append(i)
l.sort(reverse=True)
for i in l:
    print(i)