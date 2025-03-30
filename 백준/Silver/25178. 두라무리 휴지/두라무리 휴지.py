import sys
def input():
    return sys.stdin.readline()

n = int(input())
f = input().strip()
s = input().strip()
if sorted(list(f)) == sorted(list(s)):
    if f[0] == s[0] and f[-1] == s[-1]:
        if f.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','') == s.replace('a','').replace('e','').replace('i','').replace('o','').replace('u',''):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')