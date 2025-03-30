import sys
def input():
    return sys.stdin.readline()

x = int(input())
count = 0
while x >0 :
    if x >= 64:
        count +=1
        x -= 64
    elif x >= 32:
        count +=1
        x -= 32
    elif x >= 16:
        count +=1
        x -= 16
    elif x >= 8:
        count +=1
        x -= 8
    elif x >= 4:
        count +=1
        x -= 4
    elif x >= 2:
        count +=1
        x -= 2
    elif x >= 1:
        count +=1
        x -= 1
print(count)
