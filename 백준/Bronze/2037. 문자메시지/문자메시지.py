import sys
def input():
    return sys.stdin.readline()

p, w = map(int,input().strip().split())
l = list(input().strip())
dic = {' ':1,
       'A':2, 'B':22, 'C':222,
       'D':3, 'E':33, 'F':333,
       'G':4, 'H':44, 'I':444,
       'J':5, 'K':55, 'L':555,
       'M':6, 'N':66, 'O':666,
       'P':7, 'Q':77, 'R':777, 'S':7777,
       'T':8, 'U':88, 'V':888,
       'W':9, 'X':99, 'Y':999, 'Z':9999}
time = 0
k = []
for i in l:
    k.append(str(dic[i]))
for i in range(len(k)):
    try:
        if k[i][0] == k[i+1][0]:
            if k[i] == '1':
                pass
            else:
                time += w
    except:
        pass
    time += p*len(k[i])
print(time)