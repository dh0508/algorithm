import sys
def input():
    return sys.stdin.readline()

end = 123456*2 + 1
l = [True for _ in range(end)]
for i in range(2, end):
    if l[i]:
        for j in range(2*i, end, i):
            l[j] = False

while True:
    n = int(input())
    if n == 0:
        exit()
    else:
        cnt = 0
        start = n
        end = 2*n
        for i in range(start+1, end+1):
            if l[i]:
                cnt += 1
        print(cnt)