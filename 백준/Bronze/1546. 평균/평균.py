n = int(input())
score = list(map(int, input().split()))
print(sum([a / max(score) * 100 for a in score])/n)