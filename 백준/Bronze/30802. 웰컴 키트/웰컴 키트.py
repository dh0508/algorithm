n = int(input())
a,b,c,d,e,f = map(int,input().split())
t,p = map(int,input().split())
l = [a,b,c,d,e,f]
print(6 - l.count(-1) + (a-1)//t + (b-1)//t + (c-1)//t + (d-1)//t + (e-1)//t + (f-1)//t)
print(n//p, n%p)