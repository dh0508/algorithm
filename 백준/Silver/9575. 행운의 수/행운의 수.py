import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for _ in range(test_case):
    an = int(input())
    al = list(map(int,input().strip().split()))
    bn = int(input())
    bl = list(map(int,input().strip().split()))
    cn = int(input())
    cl = list(map(int,input().strip().split()))
    ps = set()
    for i in range(an):
        for j in range(bn):
            for k in range(cn):
                sum_number = al[i]+bl[j]+cl[k]
                tf = 1
                for l in str(sum_number):
                    if l in ['1','2','3','4','6','7','9','0']:
                        tf = 0
                        break
                if tf == 1:
                    ps.add(sum_number)
    print(len(ps))