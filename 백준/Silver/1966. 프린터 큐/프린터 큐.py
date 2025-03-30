test_case = int(input())
for _ in range(test_case):
    n, m = map(int,input().strip().split())
    l = list(map(int,input().strip().split()))
    count = 0
    while l:
        if m == 0:
            if l[0] == max(l):
                count += 1
                l.pop(0)
                break
            else:
                l.append(l.pop(0))
                m = len(l)-1
        else:
            if l[0] == max(l):
                count += 1
                l.pop(0)
                m -= 1
            else:
                l.append(l.pop(0))
                m -= 1
    print(count)