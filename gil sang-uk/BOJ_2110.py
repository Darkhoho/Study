import sys;input = sys.stdin.readline

n, c = map(int, input().split())
li = [int(input()) for i in range(n)]
li.sort()
s, e = 1, li[-1] - li[0]
res = 0
# 이분탐색
if c == 2:
    print(e)
else:
    while s < e:
        mid = (s + e) // 2
        # 첫 지점 공유기 설치
        curr = li[0]
        cnt = 1
        for i in range(1,n):
            # mid 이상의 거리를 두며 공유기 설치
            if li[i] >= curr + mid:
                cnt += 1
                # 설치한 자리로 재할당
                curr = li[i]
        # 다 설치한 뒤
        # 공유기가 많거나 같으면 거리를 넓혀서 설치해보기
        if cnt >= c:
            s = mid+1
            res = mid
        # 공유기가 적게 설치 되었으면 거리를 좁혀서 설치
        else:
            e = mid
    print(res)