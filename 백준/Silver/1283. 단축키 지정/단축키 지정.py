import sys
def input():
    return sys.stdin.readline().strip()  # 개행문자 제거

def isin(a):
    a = a.lower()
    if a in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
        if a in l:
            return True
        else:
            return False
    else:
        return True

l = []
N = int(input())
for _ in range(N):
    isprint = False
    a = input()
    b = list(a.split())

    for i in range(len(b)):
        if not isin(b[i][0]):
            l.append(b[i][0].lower())
            print(" ".join("[" + b[j][0] + "]" + b[j][1:] if j == i else b[j]
                for j in range(len(b))))
            isprint = True
            break

    if not isprint:
        for i in range(len(a)):
            if not isin(a[i]):
                l.append(a[i].lower())
                print(a[:i] + "[" + a[i] + "]" + a[i+1:])
                isprint = True
                break

    if not isprint:
        print(a)
