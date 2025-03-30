import sys
def input():
    return sys.stdin.readline()

for _ in range(int(input())):
    a, b = input().strip().split()
    al = list(a)
    bl = list(b)
    al.sort()
    bl.sort()
    if al == bl:
        print(a,"&", b, "are anagrams.")
    else:
        print(a,"&", b, "are NOT anagrams.")