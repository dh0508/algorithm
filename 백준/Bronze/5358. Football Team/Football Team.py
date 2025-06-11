while True:
    try:
        a = input().strip()
        b = (
            a.replace('i', '0')
             .replace('I', '2')
             .replace('e', '1')
             .replace('E', '3')
             .replace('0', 'e')
             .replace('2', 'E')
             .replace('1', 'i')
             .replace('3', 'I')
        )
        print(b)
    except EOFError:
        break
