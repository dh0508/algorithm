import sys
def input():
    return sys.stdin.readline()

h,m = map(int,input().split())
pm = int(input())

if (m+pm)//60 >= 1:
    if (h+(m+pm)//60)>=1:
        print((h+(m+pm)//60)%24,(m+pm)%60)
    else:
        print(h+(m+pm)//60,(m+pm)%60)
else:
    print(h,m+pm)