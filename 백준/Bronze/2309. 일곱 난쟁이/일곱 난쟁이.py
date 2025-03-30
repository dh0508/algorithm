import sys
def input():
    return sys.stdin.readline()

l = []
for _ in range(9):
    l.append(int(input().strip()))
def solution():
    for i in range(9):
        for j in range(i+1,9):
            ll = l[::]
            ll.remove(l[i])
            ll.remove(l[j])
            if sum(ll) == 100:
                ll.sort()
                for k in ll:
                    print(k)
                return
solution()