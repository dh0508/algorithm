import sys
def input():
    return sys.stdin.readline()

N = int(input())
if N < 10:
    print(1)
else:
    if N // 9 % 2 == 0:
        if N % 9 == 0:
            print(N//9)
        else:
            print(N//9+1)
    else:
        if N % 9 == 0:
            print(N//9)
        else:
            if N % 9 % 2 == 0:
                print(N//9+2)
            else:
                print(N//9+1)