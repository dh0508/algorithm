import sys
def input():
    return sys.stdin.readline()

a = int(input())
b = input().replace('\n','')
b_ = str(b)
print(int(b_[-1])*a)
print(int(b_[-2])*a)
print(int(b_[-3])*a)
print(a*int(b))