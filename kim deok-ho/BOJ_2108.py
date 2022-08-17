import sys
input = sys.stdin.readline

# 방법1

# 수의 개수
N = int(input())

# 입력 받은 수를 양수와 음수로 나워서 저장
plusNums = [0]*4001
minusNums = [0]*4001

# 입력된 값의 합(산술평균)
numSum = 0

# 양수, 음수 입력 횟수(중앙값)
plusCnt = 0
minusCnt = 0

# 중앙값 위치
center = N//2 + 1

# 음수, 양수 최빈 횟수(최빈값)
minusMode = 0
plusMode = 0

# 최댓값, 최솟값(범위)
maxNum = -4000
minNum = 4000

# 숫자의 개수만큼 반복
for _ in range(N):
    n = int(input())

    # 최댓값, 최솟값 저장(범위)
    if maxNum < n:
        maxNum = n
    if minNum > n:
        minNum = n

    # 음수 입력
    if n < 0:
        # 해당 정수 입력받은 횟수 저장(최빈값)
        minusNums[-n] += 1
        # 음수 입력 횟수(중앙값)
        minusCnt += 1
        # 정수 누적 합(산술평균)
        numSum += n
        # 음수 중 최빈 횟수 저장(최빈값)
        if minusMode < minusNums[-n]:
            minusMode = minusNums[-n]
    # 0과 양수 입력
    else:
        # 해당 정수 입력받은 횟수 저장(최빈값)
        plusNums[n] += 1
        # 양수 입력 횟수(중앙값)
        plusCnt += 1
        # 정수 누적 합(산술평균)
        numSum += n
        # 양수 중 최빈 횟수 저장(최빈값)
        if plusMode < plusNums[n]:
            plusMode = plusNums[n]

# 산술평균
ans = round(numSum/N)
print(f'{int(ans)}')

# 중앙값
# 중앙값이 양수에 있는 경우
if center > minusCnt:
    # 양수의 몇 번째 숫자인지 확인
    order = center - minusCnt
    # 0부터 4000까지 확인
    for i in range(4001):
        # 숫자가 있다면
        if plusNums[i] > 0:
            # 입력받은 횟수만큼 저장된 order 에서 1 빼기
            for _ in range(plusNums[i]):
                order -= 1
                # idx 가 0이 된다면 해당 위치 인덱스 출력
                if order == 0:
                    print(i)
                    break
# 음수에 있는 경우
else:
    order = center
    # -4000부터 -1까지 확인
    for i in range(4000, 0, -1):
        # 숫자가 있으면
        if minusNums[i] > 0:
            # 입력받은 횟수만큼 저장된 order 에서 1 빼기
            for _ in range(minusNums[i]):
                order -= 1
                if order == 0:
                    # 음수이기 때문에 -붙여서 출력
                    print(-i)
                    break

# 최빈값
# 최빈값을 담아둘 리스트
modeNum = []
# 최빈값이 음수에 있는 경우
if minusMode > plusMode:
    # -4000부터 -1까지 확인
    for i in range(4000, 0, -1):
        if minusNums[i] == minusMode:
            modeNum.append(-i)
            # 최빈값이 2개가 되면 해당 정수 출력
            if len(modeNum) == 2:
                print(-i)
                break
    # 최빈값이 1개면 저장된 값 출력
    else:
        print(modeNum[0])

# 최빈값이 양수에 있는 경우
elif plusMode > minusMode:
    # 1부터 4000까지
    for i in range(4001):
        if plusNums[i] == plusMode:
            modeNum.append(i)
            # 최빈값이 2개가 되면 해당 정수 출력
            if len(modeNum) == 2:
                print(i)
                break
    # 1개이면 저장된 정수 출력
    else:
        print(modeNum[0])

# 최빈값이 음수, 양수 모두 있는 경우
else:
    # 음수에서 최빈값 찾기
    for i in range(4000, 0, -1):
        if minusNums[i] == minusMode:
            modeNum.append(-i)
            # 음수에서 이미 최빈값이 2개가 되면 해당 값 출력
            if len(modeNum) == 2:
                print(-i)
                break
    # 음수에 1개만 있다면 양수에서 1개 찾기
    if len(modeNum) == 1:
        for i in range(4001):
            if plusNums[i] == plusMode:
                print(i)
                break

# 범위
print(maxNum-minNum)

# 방법 2 - 함수 사용
# 수의 개수
N = int(input())

# 산술 평균
avg = 0

# 최댓값, 최솟값
maxNum = -4000
minNum = 4000

# 입력받은 정수
nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)
    avg += num
    if maxNum < num:
        maxNum = num
    if minNum > num:
        minNum = num

# 산술평균
print(int(round(avg/N)))

# 중앙값
nums.sort()
print(nums[N//2])

# 최빈값
if len(nums) == 1:
    print(nums[0])
else:
    mode = {}
    for i in range(N):
        mode[nums[i]] = mode.get(nums[i], 0) + 1

        # 같은 내용 다른 방법
        # if nums[i] in mode:
        #     mode[nums[i]] += 1
        # else:
        #     mode[nums[i]] = 1

    # 최빈 횟수
    maxMode = max(mode.values())

    maxModeList = []
    for k, val in mode.items():
        if val == maxMode:
            maxModeList.append(k)

    if len(maxModeList) == 1:
        print(maxModeList[0])
    else:
        maxModeList.sort()
        print(maxModeList[1])

# 범위
print(maxNum - minNum)