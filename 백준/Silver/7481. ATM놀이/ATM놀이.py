import sys
def input():
    return sys.stdin.readline()

T = int(input())
for _ in range(T):
    a, b, S = map(int, input().strip().split())
    if a > b:
        big = a
        small = b
    else:
        small = a
        big = b
    smallnumcount = 0
    bignumcount = 0
    if small % 2 == 0 and big % 2 == 0 and S % 2 != 0:
        print("Impossible")
        continue
    for i in range(S//big, 0, -1):
        if (S-(big*i))%small == 0:
            bignumcount = i
            break
    smallnumcount = (S-(big*bignumcount))//small
    if big*bignumcount + small*smallnumcount != S:
        print("Impossible")
    else:
        if big == a:
            print(bignumcount, smallnumcount)
        else:
            print(smallnumcount, bignumcount)