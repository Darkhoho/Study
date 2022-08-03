# 높이의 수, 수열의 크기
num = int(input())

# 측정한 높이를 리스트에 저장
heights = list(map(int, input().split()))

# 시작 인덱스와 끝 인덱스를 튜플로 묶어서 담을 리스트 선언
idxList = []
# 인덱스 0부터 시작
idx = 0
# 인덱스가 num-2까지만 반복(n-1이 마지막 인덱스이기 때문에 다음 인덱스와 비교할 수 없음)
while idx <= num-2:
    # 만약 인덱스가 num-2이고 마지막 값이 더 크면 현재 인덱스를 시작값, 마지막 인덱스를 끝값으로 튜플로 묶어서 리스트에 추가
    if idx == num-2 and heights[idx] < heights[idx+1]:
            start = idx
            end = idx+1
            idxList.append((start, end))
            break
    # 인덱스가 n-2보다 작고 현재 인덱스의 값과 다음 인덱스 값을 비교해서 다음 인덱스가 크면 현재 인덱스를 시작값으로 저장
    elif heights[idx] < heights[idx+1]:
        start = idx
        # 인덱스를 증가해가면서 반복
        while True:
            idx += 1
            # 인덱스가 num-2 보다 작고 현재 인덱스의 값 보다 다음 값이 작거나 같아지면 오르막길이 끝났으니 현재의 인덱스를 끝값으로 튜플로 묶어서 리스트에 추가
            if idx <= num-2 and heights[idx] >= heights[idx+1]:
                end = idx
                idxList.append((start, end))
                idx += 1
                break
            # 인덱스가 num-2일 때 마지막 인덱스 값과 비교해서 오르막길이 끝나지 않음
            # 그렇기에 마지막 인덱스의 값을 끝 값으로 튜플로 묶어서 리스트에 추가
            elif idx == num-2:
                idx += 1
                end = idx
                idxList.append((start, end))
                break
    # 오르막길이 아니면 다음 인덱스를 확인
    else:
        idx += 1

# 오르막길이 없다면 0을 출력
if len(idxList) == 0:
    print(0)

# 오르막길이 있다면 각 오르막길의 크기를 구해서 최댓값을 찾아 출력
else:
    result = []
    for x, y in idxList:
        result.append(heights[y] - heights[x])
    print(max(result))


# 방법2

# 높이의 수, 수열의 크기
num = int(input())

# 측정한 높이를 리스트에 저장
heights = list(map(int, input().split()))

# 오르막길의 차이를 누적하는 변수 선언
result = 0
# 누적된 오르막길의 차이를 담을 리스트 선언
results = []
cnt = 0
# 1부터 시작해서 그 전의 값과 비교해서 오르막길이면 그 차이를 변수에 누적
for idx in range(1, num):
    if heights[idx-1] < heights[idx]:
        result += (heights[idx] - heights[idx-1])
    # 오르막길이 끝나거나 오르막길이 아니면 누적된 차이를 리스트에 추가하고 값을 초기화
    else:
        results.append(result)
        cnt += 1
        result = 0
# 마지막까지 반복문을 다 돌았다면 마지막에 저장된 값을 리스트에 추가
results.append(result)
cnt += 1
# 최댓값 출력
print(max(results))

# max 함수 이용하지 않고 최댓값 출력
maxResult = results[0]
for idx in range(1, cnt):
    if results[idx] > maxResult:
        maxResult = results[idx]
print(maxResult)