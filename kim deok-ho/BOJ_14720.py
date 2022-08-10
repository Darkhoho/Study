# 딸기우유0, 초코우유1, 바나나우유2
# 우유 가게의 수
num = int(input())
# 우유 가게의 판매 리스트
stores = list(map(int,input().split()))
# 현재 먹을 수 있는 우유
now = 0
# 우유를 먹은 횟수
cnt = 0
# 판매하는 우유와 현재 먹을 수 있는 우유가 같다면 횟수를 추가
for store in stores:
    # 판매 우유와 현재 먹을 수 있는 우유가 같고 바나나 우유를 먹었다면
    # 먹을 수 있는 우유를 딸기 우유로 바꾸고 횟수를 추가
    if now == store and now == 2:
        cnt += 1
        now = 0
    # 그 외에 일치하면 횟수와 다음 우유로 바꾼다.
    elif now == store:
        cnt += 1
        now += 1
print(cnt)