import sys

# 입력의 최대값이 10,000이므로 이 크기의 리스트를 만들어줍니다.
count = [0] * 10001

# 입력의 개수(N)를 읽어옵니다.
N = int(sys.stdin.readline().strip())

# 주어진 숫자들을 카운트 배열에 기록합니다.
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    count[num] += 1

# 카운트 배열을 순회하면서 결과를 출력합니다.
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)