m = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    count = 0
    a = input()
    if a == '#':
        break
    for s in a:
        if s in m:
            count += 1
    print(count)