import sys
def input():
    return sys.stdin.readline()

countA, countB, maxA, maxB = map(int, input().strip().split())

if countA < countB:
    countA, countB = countB, countA
    maxA, maxB = maxB, maxA

if countA == 0 or maxA == 0:
    print(min(countB, maxB))
elif countB == 0 or maxB == 0:
    print(min(countA, maxA))

else:
    if countA < countB + 1:
        print(countB * 2)
    elif countA == countB + 1:
        print(countA + countB)
    else:
        print(min((countB + 1) * maxA, countA) + countB)