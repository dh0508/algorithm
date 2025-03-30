import sys

def input():
    return sys.stdin.readline().strip()

a = list(input())

def solution(a):
    i = 0
    while i < len(a):
        if a[i] == '*' or a[i] == '/':
            l = a[i-1]
            r = a[i+1]
            a[i-1:i+2] = [str(l + r + a[i])]
            i -= 1
        else:
            i += 1
    i = 0
    while i < len(a):
        if a[i] == '+' or a[i] == '-':
            l = a[i-1]
            r = a[i+1]
            a[i-1:i+2] = [str(l + r + a[i])]
            i -= 1
        else:
            i += 1
    return a

def process_parentheses(a):
    while ')' in a:
        r = a.index(')')
        l = r - a[:r][::-1].index('(') - 1
        a[l:r+1] = solution(a[l+1:r])
    return solution(a)

a = process_parentheses(a)
print(''.join(a))
