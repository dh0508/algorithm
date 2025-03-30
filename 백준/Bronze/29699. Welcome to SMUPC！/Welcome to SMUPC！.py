import sys
def input():
    return sys.stdin.readline()

a = "WelcomeToSMUPC"
N = int(input())
N %= 14
print(a[N-1])