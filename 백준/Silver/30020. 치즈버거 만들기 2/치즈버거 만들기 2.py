import sys
def input():
    return sys.stdin.readline()

A, B = map(int,input().strip().split())
if (A <= B) or (A-B > B):
    print("NO")
    exit()
print("YES")
print(A-B)
for i in range(A-B):
    if i == A-B-1:
        print("a"+"ba"*(B-A+B+1))
    else:
        print("aba")