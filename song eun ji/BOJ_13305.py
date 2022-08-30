#도시개수
T = int(input())

#km랑 l 값 받기
km = list(map(int,input().split()))
l = list(map(int,input().split()))

#초기화
total_km = 0
start_l = l[0]

#리터 계산하기
total_money = start_l*km[0]
for i in range(1,T-1):
    if start_l > l[i]:
        start_l = l[i]
    total_money = start_l * km[i] # 한 지역을 갈때 필요한 가격을 더함

print(total_money)