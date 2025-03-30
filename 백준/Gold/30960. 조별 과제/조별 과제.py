import sys
def input():
    return sys.stdin.readline()

N = int(input())
l = list(map(int,input().split()))
l.sort()

two = 0
two_and_three = float("inf")
for i in range(1, N, 2):
    two = two + l[i] - l[i - 1]
    two_and_three = min(two, two_and_three) + l[i + 1] - l[i]
print(two_and_three)