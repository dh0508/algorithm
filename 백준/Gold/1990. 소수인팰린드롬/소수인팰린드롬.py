import sys
def input():
    return sys.stdin.readline().strip()

a, b = map(int, input().strip().split())

palindrome = []
if b > 10000000:
    b = 10000000
for i in range(a, b+1):
    if str(i) == str(i)[::-1]:
        palindrome.append(i)

for i in palindrome:
    isprime = True
    if len(str(i)) % 2 == 0:
        if i == 11:
            pass
        else:
            isprime = False
    if isprime:
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                isprime = False
                break
    if isprime:
        print(i)
print(-1)