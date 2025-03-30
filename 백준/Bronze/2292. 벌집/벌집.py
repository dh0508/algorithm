a = int(input())-1
b = 1
for i in range(1,10000000):
    b = 6*i
    if a > b:
        a -= b
    else:
        break
if a == 0:
    print(1)
else:
    print(i+1)