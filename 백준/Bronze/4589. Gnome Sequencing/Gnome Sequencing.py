t =int(input())
print("Gnomes:")
for _ in range(t):
    a,b,c = map(int, input().strip().split())
    if (a>b and b>c) or (a<b and b<c):
        print("Ordered")
    else:
        print("Unordered")