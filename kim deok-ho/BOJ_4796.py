# P일 중에 L일 사용 가능하고 P-L일 사용 불가
# 케이스 넘버
n = 0
while True:
    # l = 사용 가능 일수, p = 연속 일수 v = 휴가 기간
    l, p, v = map(int, input().split())
    if v != 0:
        n += 1
        # 이용 횟수
        # 휴가 일수를 연속 일수로 나누고 사용 가능 일수로 곱하면 이용 횟수가 된다.
        cnt = (v // p)*l
        # 나머지가 l 보다 크거나 같으면 l을 더하고 작으면 나머지를 더한다.
        cnt = (cnt + l) if v%p >= l else (cnt + v%p)
        print(f'Case {n}: {cnt}')
    # 휴가 일수가 0이면 반복문 종료
    else:
        break