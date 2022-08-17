# 방법 1
# 국가의 수, 알고 싶은 국가
n, k = map(int, input().split())
# 국가별 금, 은, 동 개수
nation = [list(map(int, input().split())) for _ in range(n)]

# 1등부터 시작
rank = 1

for i in range(n):
    # 목표 국가인 경우
    if nation[i][0] == k:
        # 다른 국가와 비교
        for j in range(n):
            # 금메달이 많으면 1 증가
            if nation[j][1] > nation[i][1]:
                rank += 1
            # 금메달 수는 같고 은메달이 많으면 1 증가
            elif nation[j][1] == nation[i][1] and nation[j][2] > nation[i][2]:
                rank += 1
            # 금메달, 은메달이 같고 동메달이 많으면 1 증가
            elif nation[j][1] == nation[i][1] and nation[j][2] == nation[i][2] and nation[j][3] > nation[i][3]:
                rank += 1
        print(rank)

# 방법 2 - 타겟을 따로 분리
# 국가의 수, 알고 싶은 국가
n, k = map(int, input().split())
# 국가 리스트와 타겟 리스트 초기화
nations = []
target = []
# 타겟은 타겟 리스트에 넣고 나머지 국가는 국가 리스트에 추가
for i in range(n):
    nation = list(map(int, input().split()))
    if nation[0] == k:
        target.append(nation)
    else:
        nations.append(nation)

# 1등부터 시작
rank = 1
for i in range(n-1):
    # 타겟보다 금메달 많은 국가가 있으면 1 증가
    if nations[i][1] > target[0][1]:
        rank += 1
    # 금메달은 같고 은메달이 많은 국가가 있으면 1 증가
    elif nations[i][1] == target[0][1] and nations[i][2] > target[0][2]:
        rank += 1
    # 금, 은 같고 동이 많은 국가가 있으면 1 증가
    elif nations[i][1] == target[0][1] and nations[i][2] == target[0][2] and nations[i][3] > target[0][3]:
        rank += 1
print(rank)