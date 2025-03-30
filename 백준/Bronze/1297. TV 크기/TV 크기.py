import sys
def input():
    return sys.stdin.readline()

D, H, W = map(int,input().strip().split())
b = ((W*W*D*D)/(H*H+W*W))**(1/2)
a = H*b/W
print(int(a),int(b))