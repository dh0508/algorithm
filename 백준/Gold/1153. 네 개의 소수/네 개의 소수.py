import sys
def input():
    return sys.stdin.readline()

prime = [False, False] + [True for _ in range(1000000)]
for i in range(2, int(1000000**0.5)+1):
    if prime[i]:
        for j in range(i*2, 1000000, i):
            prime[j] = False

N = int(input())
prime_num = [i for i in range(1000000) if prime[i]]
prime_num_set = set(prime_num)

for i in range(len(prime_num)):
    if prime_num[i] > N:
        break
    for j in range(i, len(prime_num)):
        if prime_num[i] + prime_num[j] > N:
            break
        for k in range(j, len(prime_num)):
            if prime_num[i] + prime_num[j] + prime_num[k] > N:
                break
            remaining = N - (prime_num[i] + prime_num[j] + prime_num[k])
            if remaining in prime_num_set:
                print(prime_num[i], prime_num[j], prime_num[k], remaining)
                exit()
print(-1)