def minusDirection(cnt, arr):         # 음수 방향
    walk = 0
    nowPosition = 0                   # 현 위치
    for i in range(cnt-1, -1, -1):    # 가까운 곳으로 이동
        if cnt <= M:                  # 옮길 책이 옮길 수 있는 책보다 적은 경우
            walk += arr[i] - nowPosition
            nowPosition = arr[i]
            cnt -= 1
        else:                         # 옮길 책이 더 많은 경우
            if cnt % M:               # 옮길 수 있는 책 개수로 나눠지지 않는 경우
                walk += ((arr[i] - nowPosition) * 2*(cnt//M)) + (arr[i] - nowPosition) # 왕복하고 한 번 더 움직임
                nowPosition = arr[i]  # 현 위치
                cnt -= 1              # 옮길 책 -1
            else:                     # 나눠지는 경우
                walk += ((arr[i] - nowPosition) * 2*(cnt//M)) - (arr[i] - nowPosition) # 왕복하고 한 번 덜 움직임
                nowPosition = arr[i]
                cnt -= 1
    return walk

def plusDirection(cnt, arr):                # 양수 방향
    walk = 0
    nowPosition = 0
    for i in range(cnt):
        if cnt <= M:
            walk += arr[i] - nowPosition
            nowPosition = arr[i]
            cnt -= 1
        else:
            if cnt % M:
                walk += ((arr[i] - nowPosition) * 2*(cnt//M)) + (arr[i] - nowPosition)
                nowPosition = arr[i]
                cnt -= 1
            else:
                walk += ((arr[i] - nowPosition) * 2*(cnt//M)) - (arr[i] - nowPosition)
                nowPosition = arr[i]
                cnt -= 1
    return walk

N, M = map(int, input().split())        # N: 옮길 책 권수, M: 들 수 있는 책 권수
position = list(map(int, input().split()))
position.sort()

minuCnt = 0                             # 음수, 양수 개수
plusCnt = 0

minus = []                              # 음수 리스트, 양수 리스트
plus = []

for i in range(N):                      # 음수, 양수 개수를 세고 따로 분류
    if position[i] < 0:
        minuCnt += 1
        minus.append(-position[i])
    else:
        plusCnt += 1
        plus.append(position[i])

if plusCnt == 0:                        # 음수만 있는 경우
    print(minusDirection(minuCnt, minus))

elif minuCnt == 0:                      # 양수만 있는 경우
    print(plusDirection(plusCnt, plus))

else:                                   # 둘 다 있는 경우
    if minus[0] > plus[-1]:             # 음수가 더 먼 경우
        ans = plusDirection(plusCnt, plus)
        ans += plus[-1]
        ans += minusDirection(minuCnt, minus)
        print(ans)
    else:                               # 양수가 더 먼 경우
        ans = minusDirection(minuCnt, minus)
        ans += minus[0]
        ans += plusDirection(plusCnt, plus)
        print(ans)




