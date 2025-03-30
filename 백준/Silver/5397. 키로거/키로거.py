import sys
def input():
    return sys.stdin.readline()

test_case = int(input())
for _ in range(test_case):
    password = list(input().strip())
    left = []
    right = []

    for i in password:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(*left, sep='')