import sys
def input():
    return sys.stdin.readline()

while True:
    try:
        N = int(input())
        ans = 1

        for i in range(1, N + 1):
            ans *= i
            ans = int(str(ans).rstrip('0'))
            ans %= 10**9

        print(f"{N:5} -> {str(ans)[-1]}")
    except:
        break