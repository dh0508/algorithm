import sys
def input():
    return sys.stdin.readline()

l = []
for _ in range(8):
    l.append(int(input().strip()))

ll = sorted(l)
hpn = []
print(ll[-1]+ll[-2]+ll[-3]+ll[-4]+ll[-5])
for i in l:
    if i == ll[-1] or i == ll[-2] or i == ll[-3] or i == ll[-4] or i == ll[-5]:
        hpn.append(l.index(i)+1)
print(*hpn)