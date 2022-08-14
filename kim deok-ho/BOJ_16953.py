# a는 초기값 b는 결과값
a, b = map(int, input().split())

# 계산 횟수
cnt = 0

# 결과값을 초기값으로 다시 바꿔가면서 계산 횟수 증가
while True:
    # 결과값의 마지막 숫자가 홀수이면서 1이 아니면 -1 출력
    # 홀수이면 끝이 1이기 때문에 10으로 나눠 1을 떨어뜨리기
    if b % 2:
        if b%10 != 1:
            print(-1)
            break
        b = b//10
        # 계산 횟수 1 증가
        cnt += 1
    # 짝수이면 2로 나누기
    else:
        b = b//2
        # 계산 횟수 1 증가
        cnt += 1
    # 결과값이 초기값 보다 크다면 다시 반복
    if b > a:
        continue
    # 결과값이 초기값이 되었다면 횟수에 1을 더하고 출력하고 반복 종료
    elif b == a:
        print(cnt+1)
        break
    # 결과값이 초기값 보다 작아지면 -1 출력하고 반복 종료
    else:
        print(-1)
        break