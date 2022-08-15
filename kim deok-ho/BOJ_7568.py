# 전체 사람 수
n = int(input())
# 사람들의 덩치
people = [tuple(map(int, input().split())) for _ in range(n)]
# [(무게, 키), (무게, 키), (무게, 키), (무게, 키)]

# 사람들 모두 확인
for i in range(n):
    rank = 1
    # 다른 사람과 비교
    for j in range(n):
        # 몸무게가 크고 키가 더 크면 덩치가 큰 것
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    print(rank, end=' ')
print()

