import sys
input = sys.stdin.readline
N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()
if C == 2:                                                  # 집이 2개인 경우
    print(house[-1] - house[0])                             # 가장 끝 집과 가장 앞 집에 설치
    
else:
    s = 1                                                   # 공유기 설치 최소 거리
    e = house[N-1] - house[0]                               # 공유기 설치 최대 거리
    ans = 0
    while s <= e:
        installed = house[0]                                # 공유기가 설치된 집
        cnt = 1
        m = (s + e) // 2                                    # 설치 가능 거리 중간값
        for i in range(1, N):
            if house[i] - installed >= m:                   # 두 집 사이 거리가 중간값 이상이면 공유기 설치
                cnt += 1
                installed = house[i]
                
        if cnt >= C:                        # 공유기 설치 횟수가 공유기 개수보다 많거나 같으면
            s = m+1                         # 최소 거리를 조정
            ans = m                         # 현재 거리 저장
                                            # 공유가 설치 횟수가 개수보다 많으면 같아지는 경우에 다시 저장됨
                                            # 거리를 늘렸기 때문에 횟수가 같거나 줄어드는 경우만 있음
                                            # 설치 횟수가 같아지더라도 설치 거리가 더 큰 경우가 있을 수 있음

        elif cnt < C:                       # 공유기 설치 횟수가 공유기 개수보다 작으면
            e = m-1                         # 최대 거리를 조정
    print(ans)