p_change = {'A+':4.5, 
           'A0':4.0, 
           'B+':3.5, 
           'B0':3.0, 
           'C+':2.5, 
           'C0':2.0, 
           'D+':1.5,
           'D0':1.0,
           'F':0.0,
           }
h_l = []
p_l = []
for i in range(20):
    a, h, p = input().strip().split()
    if p == 'P':
        pass
    else:
        h_l.append(float(h))
        p_l.append(p_change[p])
s=0

for i in range(len(h_l)):
    s += h_l[i] * p_l[i]
print(s/sum(h_l))