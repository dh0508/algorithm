while True:
    a, b, c = map(int,input().split())
    if a==0 or b==0 or c==0:
        break
    elif a**2 + c**2 == b**2:
        print('right')
    elif c**2 + b**2 == a**2:
        print('right')
    elif a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')