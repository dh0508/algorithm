import sys
def input():
    return sys.stdin.readline()

def solution():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            if a*10 + b + c*10 + d == e*10 + f:
                                if dic[a]+dic[b]+dic[c]+dic[d]+dic[e]+dic[f] == n_number:
                                    print(a,b,'+',c,d,'=',e,f, sep='')
                                    return
    print('impossible')


dic = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6, 0:6}
n = int(input())
n_number = n-4
solution()
