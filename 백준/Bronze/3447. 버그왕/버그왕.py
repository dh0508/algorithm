import sys
def input():
    return sys.stdin.readline()

enter_count = 0
while enter_count != 5:
    a = input().strip()
    if a == '':
        print('')
        enter_count += 1
    else:
        while 'BUG' in a:
            a = a.replace('BUG', '')
        print(a)