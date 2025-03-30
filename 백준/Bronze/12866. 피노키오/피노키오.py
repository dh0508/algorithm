import sys
def input():
    return sys.stdin.readline()

L = int(input())
l = list(input())
print(l.count("A")*l.count("C")*l.count("G")*l.count("T")%1000000007)