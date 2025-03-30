house_cnt = int(input())
house_price_list = []

for i in range(house_cnt):
    house_price = list(map(int, input().split()))
    house_price_list.append(house_price)

sum_house = []
def plus (fr, sc):
    global sum_house
    sum_house = [y + min(fr) for y in sc]
    min_fr = min(fr)
    min_cnt = int(fr.index(min_fr))
    del fr [fr.index(min_fr)]
    sum_house[min_cnt] = sc[min_cnt] + min(fr)
    #print(sum_house)
    return sum_house


fr_house = house_price_list[0]
sc_house = house_price_list[1]
sum_house = plus(fr_house, sc_house)

for i in range(2, house_cnt):

    plus(sum_house, house_price_list[i])

print(min(sum_house))