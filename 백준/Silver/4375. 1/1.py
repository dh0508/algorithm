import sys
def input():
    return sys.stdin.readline()

while True:
    try:
        n = int(input())
        num = 0
        for i in range(1, 10001):
            num = (num * 10 + 1) % n
            if num == 0:
                print(i)
                break
    except:
        break
