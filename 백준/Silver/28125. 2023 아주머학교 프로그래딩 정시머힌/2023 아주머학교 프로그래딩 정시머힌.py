import sys
def input():
    return sys.stdin.readline().rstrip()

d = {
    '@': 'a',
    '[': 'c',
    '!': 'i',
    ';': 'j',
    '^': 'n',
    '0': 'o',
    '7': 't'
}

N = int(input())
for _ in range(N):
    a = input()
    origin_cnt = 0
    ch_cnt = 0
    ans = ''
    i = 0
    while i < len(a):
        if a[i] == '\\' and a[i+1] == '\\' and a[i+2] == "'":
            ans += 'w'
            ch_cnt += 1
            i += 3
        elif a[i] == '\\' and a[i+1] == "'":
            ans += 'v'
            ch_cnt += 1
            i += 2
        elif a[i] in d:
            ans += d[a[i]]
            ch_cnt += 1
            i += 1
        else:
            ans += a[i]
            if a[i].isalpha():
                origin_cnt += 1
            i += 1

    total = origin_cnt + ch_cnt
    if ch_cnt * 2 >= total:
        ans = "I don't understand"

    print(ans)