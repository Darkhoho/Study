N = int(input())

milk_shops = list(map(int,input().split()))

milk = 0
count_milk = 0
for shop in milk_shops:
  if shop == milk:
    count_milk += 1
    milk += 1
    if milk == 3:
      milk = 0
print(count_milk)

  
