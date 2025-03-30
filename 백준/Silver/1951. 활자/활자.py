import sys
def input():
    return sys.stdin.readline()

n = int(input())
p = 0
ten = 1 * 10 ** (len(str(n))-1)
ten_count = len(str(n))
nine = 9
for i in range(1, ten_count+1):
    if i == ten_count:
        p += (n-ten+1) * i
    else:
        p += nine * i
        nine *= 10
print(p % 1234567)