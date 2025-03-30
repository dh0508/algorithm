import sys
def input():
    return sys.stdin.readline()

while True:
    a = input().replace('\n', '')
    l = []
    if a =='.':
        break
    for i in a:
        if i == '(':
            l.append('(')
        elif i == '[':
            l.append('[')
        elif i == ')':
            l.append(')')
        elif i == ']':
            l.append(']')
    l = ''.join(l)
    while '()' in l or '[]' in l:
        l = l.replace('()', '')
        l = l.replace('[]','')
    if l == '':
        print('yes')
    else:
        print('no')