import sys
def input():
    return sys.stdin.readline()

n = int(input())
m = int(input())
s = input()
answer = 0
c = 0
i = 0
while ( i < m ) :
    if s[i:i+3] == 'IOI':
        i += 2
        c += 1
        if c == n :
            answer += 1
            c -= 1
    else:
        i += 1
        c = 0
    
print(answer)