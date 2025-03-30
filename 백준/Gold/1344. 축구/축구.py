import sys
def input():
    return sys.stdin.readline()

import math

a_team = int(input())/100
b_team = int(input())/100
a_percent = 0
b_percent = 0
l = [2,3,5,7,11,13,17]

for i in l:
    a_percent += math.comb(18, i) * a_team ** i * (1-a_team) ** (18-i)
    b_percent += math.comb(18, i) * b_team ** i * (1-b_team) ** (18-i)

print(a_percent + b_percent - (a_percent * b_percent))