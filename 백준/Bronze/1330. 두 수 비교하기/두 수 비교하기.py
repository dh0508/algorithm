s = list(map(int, input().strip().split(' ')))
if s[0] > s[1]:
    print('>')
elif s[0]< s[1]:
    print('<')
else:
    print('==')