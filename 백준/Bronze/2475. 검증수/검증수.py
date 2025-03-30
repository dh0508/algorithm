from functools import reduce

a= list(map(int, input().split()))
b = [num*num for num in a]
print((reduce(lambda x, y : x+y, b))%10)