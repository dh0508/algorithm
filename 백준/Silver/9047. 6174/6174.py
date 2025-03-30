T = int(input())
for _ in range(T):
    N = int(input().strip())
    cnt = 0
    while N != 6174:
        N = list(str(N))
        N.sort(reverse=True)
        big = int(''.join(N))
        N.sort()
        small = int(''.join(N))
        N = big - small
        cnt += 1
        if N < 1000:
            N = N * 10

    print(cnt)
