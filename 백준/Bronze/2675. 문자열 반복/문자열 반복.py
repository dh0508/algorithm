testcase = int(input())

for i in range(testcase):
    a, b = tuple(map(str, input().split()))
    print(''.join([b[i]*int(a) for i in range(len(b))]))