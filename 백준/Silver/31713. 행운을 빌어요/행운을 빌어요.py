import sys
def input():
    return sys.stdin.readline()

T = int(input())
for _ in range(T):
    A, B = map(int, input().strip().split())
    ans = 0
    while A * 4 < B:
        A += 1
        ans += 1
    if 3 * A > B:
        ans += 3 * A - B

    print(ans)