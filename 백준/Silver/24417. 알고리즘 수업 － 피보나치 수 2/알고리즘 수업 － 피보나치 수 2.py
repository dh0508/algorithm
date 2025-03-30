import sys
def input():
    return sys.stdin.readline()


n = int(input())
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
for i in range(17, 44):
    fibonacci.append(fibonacci[i]+fibonacci[i-1])

for i in range(45, n+1):
    nb = i%45
    fibonacci[nb] = (fibonacci[nb-1]+fibonacci[nb-2])%1000000007

print(fibonacci[n%45], n-2)