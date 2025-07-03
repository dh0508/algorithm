import sys
def input():
    return sys.stdin.readline()

a, b, c = map(int, input().strip().split())
if a+b+c >= 100:
    print("OK")
elif a < b and a < c:
    print("Soongsil")
elif b<a and b<c:
    print("Korea")
elif c<a and c<b:
    print("Hanyang")