import sys
def input():
    return sys.stdin.readline()

N, d = map(int, input().split())
dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for i in range(1,1+N):
    a = list(str(i))
    for j in a:
        dic[int(j)] += 1
print(dic[d])