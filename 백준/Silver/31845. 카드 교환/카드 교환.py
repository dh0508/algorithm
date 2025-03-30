import sys
def input():
    return sys.stdin.readline()

n, m = map(int,input().strip().split())
card_point_list = list(map(int,input().strip().split()))
point = 0
for i in range(m):
    try:
        if max(card_point_list) > 0:
            point += card_point_list.pop(card_point_list.index(max(card_point_list)))
            card_point_list.pop(card_point_list.index(min(card_point_list)))
        else:
            pass
    except:
        pass
print(point)