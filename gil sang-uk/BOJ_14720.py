# 가게의 수
N = int(input())
# 가게 리스트
milk_lst = list(map(int,input().split()))
# 전에 먹은 우유
drink = 2
# 먹은 숫자
cnt = 0
for i in milk_lst:
    # 전에 먹은게 바나나고 딸기를 만나면
    if drink == 2 and i == 0:
        drink = i
        cnt += 1
    # 초코먹고 바나나
    if drink == 1 and i == 2:
        drink = i
        cnt += 1
    # 딸기먹고 초코
    if drink == 0 and i == 1:
        drink = i
        cnt += 1
print(cnt)