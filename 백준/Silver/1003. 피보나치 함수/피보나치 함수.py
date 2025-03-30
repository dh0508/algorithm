import sys
def input():
    return sys.stdin.readline()
def fibonacci_count(n):
    count_zero = [0] * (n + 1)
    count_one = [0] * (n + 1)
    count_zero[0] = 1
    count_one[0] = 0
    if n > 0:
        count_zero[1] = 0
        count_one[1] = 1
    for i in range(2, n + 1):
        count_zero[i] = count_zero[i - 1] + count_zero[i - 2]
        count_one[i] = count_one[i - 1] + count_one[i - 2]

    return count_zero[n], count_one[n]
T = int(input()) 
test_cases = [int(input()) for _ in range(T)]
for n in test_cases:
    result_zero, result_one = fibonacci_count(n)
    print(result_zero, result_one)
