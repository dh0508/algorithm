h, m = map(int, input().split())
ch_time = h*60+m-45
if (ch_time//60) == -1:
    print('23', ch_time % 60)
else:
    print(ch_time//60, ch_time%60)