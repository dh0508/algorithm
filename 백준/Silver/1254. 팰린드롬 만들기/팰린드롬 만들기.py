import sys
def input():
    return sys.stdin.readline().strip()

def is_pellindrome(l):
    return l == l[::-1]

l = list(input())
for i in range(len(l)+1):
    lll = l[:i]
    lll.reverse()
    ll = l+lll
    if is_pellindrome(ll):
        print(len(l)+i)
        break