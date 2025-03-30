import sys
def input():
    return sys.stdin.readline()

n = int(input())
l = list(input().strip().split())
cheese_set = set()
for i in l:
    if i.endswith('Cheese'):
        cheese_set.add(i)
if len(cheese_set) >= 4:
    print('yummy')
else:
    print('sad')