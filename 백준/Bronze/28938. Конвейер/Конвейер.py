a=int(input())
l=list(map(int, input().strip().split()))
a=sum(l)
if a>0:
    print("Right")
elif a<0:
    print("Left")
else:
    print("Stay")