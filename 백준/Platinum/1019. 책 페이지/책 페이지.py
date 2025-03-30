import sys
def input():
    return sys.stdin.readline().strip()

N = int(input())
l = [0 for _ in range(10)]
#입력
num = 1
def tonine(N):  #마지막자리 9로 맞추고
    while N % 10 != 9:
        for i in str(N):
            l[int(i)] += num
        N -= 1
    return N

while N > 0:
    N = tonine(N)
    if N < 10: #마지막 정리
        for i in range(N + 1): 
            l[i] += num
    else:  #크면 10단위로 처리하고
        for i in range(10):
            l[i] += (N // 10 + 1) * num

    l[0] -= num #0적으니까 빼줌
    num *= 10 #단위수 올리기
    N //= 10 

print(*l)