case_cnt = int(input())
for i in range(case_cnt):
    h, w, n = map(int,input().split())
    if n > 9*h:
        pr = [n%h,n//h+1]
    else:
        pr = [n%h,0,n//h+1]
    if pr[0]==0:
        pr[0] = h
        if n > 9 * h:
            pr[1] = n//h
        else:
            pr[2] = n//h
    print(*pr, sep='')