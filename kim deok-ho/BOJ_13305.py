# 기름값이 저렴한 곳에서 기름을 넣으면 최솟값

# 도시의 개수
cityNum = int(input())
# 도시 거리 리스트
cityDistance = list(map(int, input().split()))
# 도시 기름 가격 리스트
cityOil = list(map(int, input().split()))

# 비교값으로 첫 도시 기름값 설정
lowPrice = cityOil[0]
# 총 가격 변수에 첫 도시에서 다음 도시로 가는 가격 미리 대입
totalPrice = lowPrice*cityDistance[0]

# 도시가 2개이면 첫 도시에서 기름을 다 넣으니까 그대로 출력
if cityNum == 2:
    print(totalPrice)
# 도시가 2개 이상
else:
    # 마지막 도시는 도착 도시이기 때문에 범위를 도시 개수 - 1로 둔다.
    # 기름값이 비교값 보다 크다면 비교값으로 다음 도시로 감
    for idx in range(1, cityNum-1):
        if cityOil[idx] > lowPrice:
            totalPrice += lowPrice*cityDistance[idx]
        # 기름값이 비교값 보다 적으면 지금 기름값으로 비교값을 바꾸고 계산하고 다음 도시로 간다.
        else:
            lowPrice = cityOil[idx]
            totalPrice += lowPrice*cityDistance[idx]

    print(totalPrice)