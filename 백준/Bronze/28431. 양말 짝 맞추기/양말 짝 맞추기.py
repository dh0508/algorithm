import sys
def input():
    return sys.stdin.readline()

l = [int(input()) for _ in range(5)]
ll = []
for i in range(5):
    a = l.pop(0)
    if a in ll:
        ll.pop(ll.index(a))
    else:
        ll.append(a)
print(*ll)