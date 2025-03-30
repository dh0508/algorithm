import sys
def input():
    return sys.stdin.readline()

l = []
for _ in range(5):
    l.append(int(input()))
print(sum(l))