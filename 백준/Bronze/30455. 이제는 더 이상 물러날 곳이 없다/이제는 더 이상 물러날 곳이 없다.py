import sys
def input():
    return sys.stdin.readline()

a = int(input())
if a%2 == 0:
    print("Duck")
else:
    print("Goose")