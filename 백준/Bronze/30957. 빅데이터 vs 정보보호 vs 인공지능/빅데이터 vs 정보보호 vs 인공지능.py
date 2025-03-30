import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(input())
B = 0
S = 0
A = 0
for i in range(N):
    if l[i] == 'B':
        B+= 1
    elif l[i] == 'S':
        S+= 1
    else:
        A+= 1
if B == S == A:
    print('SCU')
elif B == S > A:
    print('BS')
elif S == A > B:
    print('SA')
elif B == A > S:
    print('BA')
elif B > S and B > A:
    print('B')
elif S > B and S > A:
    print('S')
elif A > S and A > B:
    print('A')
