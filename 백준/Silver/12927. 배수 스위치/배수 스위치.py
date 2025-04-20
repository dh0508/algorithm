import sys
def input():
    return sys.stdin.readline()

a = [0] + list(input().strip())
cnt = 0
for i in range(1, len(a)):
    if a[i] == 'Y':
        cnt += 1
        for j in range(i, len(a), i):
            if a[j] == 'N':
                a[j] = 'Y'
            else:
                a[j] = 'N'
print(cnt)