# 방 번호
N = list(input())
# 방 번호 길이
rnLen = len(N)
# 정수 횟수
nums = [0]*10

# 정답
ans = 0
# 각 정수 횟수 확인
for i in range(rnLen):
    nums[int(N[i])] += 1
# 각 정수의 횟수를 통해 구매 개수 확인
for i in range(9):
    # 6일 때 9와 함께 계산
    if i == 6:
        # 6의 개수와 9의 개수를 합쳐서 홀수인 경우
        if (nums[i] + nums[9]) % 2:
            # 2로 나눈 값과 나머지를 더한 값이 구매 개수
            # 1개인 경우 값 0, 나머지 1이라 구매 개수 1개
            # 3인 경우 값 1, 나머지 1이라 구매 개수 2개
            cnt = (nums[i] + nums[9]) % 2 + (nums[i] + nums[9]) // 2
        else:
            # 짝수인 경우 2로 나눈 값이 구매 개수
            cnt = (nums[i] + nums[9]) // 2
        # 구매 개수가 저장 값 보다 크면 업데이트
        if ans < cnt:
            ans = cnt
    # 6을 제외한 나머지 수는 나온 횟수가 구매 개수
    else:
        cnt = nums[i]
        # 구매 개수가 저장 값 보다 크면 업데이트
        if ans < cnt:
            ans = cnt

print(ans)