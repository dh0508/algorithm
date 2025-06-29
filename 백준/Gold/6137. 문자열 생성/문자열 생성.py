import sys
def input():
    return sys.stdin.readline()

N = int(input())
S = []
for _ in range(N):
    S.append(input().rstrip())

T = ""
for _ in range(N):
    if len(S) == 1:
        T += S.pop(0)
    elif S[0] < S[-1]:
        T += S.pop(0)
    elif S[0] > S[-1]:
        T += S.pop(-1)
    else:
        tmp = 1
        while tmp < len(S):
            if S[tmp] == S[-(tmp+1)]:
                tmp += 1
            elif S[tmp] < S[-(tmp+1)]:
                T += S.pop(0)
                break
            elif S[tmp] > S[-(tmp+1)]:
                T += S.pop(-1)
                break
        else:
            T += S.pop(0)

for i in range(0, len(T), 80):
    print(T[i:i+80])