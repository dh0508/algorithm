while True:
    a = list(map(int,input()))
    if a == [0]:
        break
    t_f = True
    for i in range(len(a)//2):
        if a[i] == a[-(i+1)]:
            t_f = True

        else:
            t_f = False
            break
    if t_f:
        print('yes')
    else:
        print('no')
