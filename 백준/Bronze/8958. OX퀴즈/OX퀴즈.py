test_case = int(input())
for i in range(test_case):
    point = 0
    result = input().split('X')
    for j in result:
        if j == '':
            pass
        else:
            point += j.count('O')*(j.count('O')+1)/2
    print(int(point))