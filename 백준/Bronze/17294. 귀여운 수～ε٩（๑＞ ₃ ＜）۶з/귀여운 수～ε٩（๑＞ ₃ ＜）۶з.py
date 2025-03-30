import sys
def input():
    return sys.stdin.readline()

l = list(input().strip())
if len(l) != 1:
    d = int(l[0]) - int(l[1])
    f = 0
    for i in range(len(l)-1):
        if int(l[i]) - int(l[i+1]) == d:
            pass
        else:
            f = 1
            break
    if f == 1:
        print('흥칫뿡!! <(￣ ﹌ ￣)>')
    else:
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')