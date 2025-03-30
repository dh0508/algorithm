a, b = input().strip().split()
a_ = []
b_ = []
for i in range(1,4):
    a_.append(a[-i])
for i in range(1,4):
    b_.append(b[-i])
if int(''.join(a_).replace(' ', '')) > int(''.join(b_).replace(' ', '')):
    print(int(''.join(a_).replace(' ', '')))
else:
    print(int(''.join(b_).replace(' ', '')))