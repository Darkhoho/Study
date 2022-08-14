# 테스트 케이스 수
testCase = int(input())

# 테스트 케이스만큼 반복
for _ in range(testCase):
    # 통나무 개수
    woodNum = int(input())
    # 통나무 높이 리스트
    heights = list(map(int, input().split()))
    # 내림차순 정렬
    heights.sort(reverse=True)

    # 1234
    # 13   5  7 6    4 2

    # 가장 낮은 높이를 맨 앞에 두 번째는 마지막에 세 번째는 첫 번째 앞에 두는 방식으로 모두 재정렬
    sortedHeights = []
    for num in range(woodNum):
        if num % 2:
            sortedHeights += [heights[num]]
        else:
            sortedHeights = [heights[num]] + sortedHeights

    # 인접한 통나무 높이의 차이 중 최댓값 구하기
    # 1번과 2번의 차이를 비교값으로 설정
    result = sortedHeights[1] - sortedHeights[0]
    # 두 번째 높이부터 다음 높이와 비교해서 높은 것으로 비교값 변경
    for num in range(1, woodNum-1):
        if abs(sortedHeights[num+1] - sortedHeights[num]) > result:
            result = abs(sortedHeights[num+1] - sortedHeights[num])
    # 마지막 높이와 첫 높이의 차이와 저장된 차이를 비교해서 최댓값 출력
    print(max(sortedHeights[-1] - sortedHeights[0], result))