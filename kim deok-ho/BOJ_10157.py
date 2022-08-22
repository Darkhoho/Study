C, R = map(int, input().split())
arr = [[0]*C for _ in range(R)]

dr = [1, 0, -1, 0]                  # 하, 우, 상, 좌
dc = [0, 1, 0, -1]

target = int(input())

if target > C*R:                    # 전체 좌석 수보다 많으면 0
    print(0)
else:
    r, c = -1, 0                    # 시작
    d = 0                           # 방향
    for i in range(1, target+1):    # 목표까지 반복
        r += dr[d]
        c += dc[d]
        if r < 0 or r > R-1 or c < 0 or c > C-1 or arr[r][c]:   # 인덱스 범위를 벗어나거나 이미 값이 있다면
            r -= dr[d]          # 다시 뒤로 돌아감
            c -= dc[d]
            d = (d+1)%4         # 방향 전환
            r += dr[d]          # 이동
            c += dc[d]
        arr[r][c] = i           # 해당 위치에 대기 순서 대입
    print(c+1, r+1)

