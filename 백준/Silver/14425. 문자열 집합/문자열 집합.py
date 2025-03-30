N, M = map(int,input().strip().split())
s = {input().strip() : 1 for _ in range(N)}
p = 0
for _ in range(M):
    a = input().strip()
    try:
        if s[a] == 1:
            p += 1
    except:
        pass
print(p)