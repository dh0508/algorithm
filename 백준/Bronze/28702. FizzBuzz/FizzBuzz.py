def change(letter):
    if letter % 3 == 0 and letter % 5 == 0:
        return 'FizzBuzz'
    elif letter % 3 == 0 and letter % 5 != 0:
        return 'Fizz'
    elif letter % 3 != 0 and letter % 5 == 0:
        return 'Buzz'
    else:
        return letter

a= input()
try:
    a = int(a)
except:
    pass
b= input()
try:
    b = int(b)
except:
    pass
c= input()
try:
    c = int(c)
except:
    pass

if isinstance(a, int):
    r = a+3
if isinstance(b, int):
    r = b+2
if isinstance(c, int):
    r = c+1

print(change(r))