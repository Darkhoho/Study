# 방법 1
R, C = map(int, input().split())
jido = [['.']*(C+2)] + [['.'] + list(input()) + ['.'] for _ in range(R)] + [['.']*(C+2)]    # 지도 사방에 바다 추가

dr = [1, -1, 0, 0]                                      # 상하좌우 델타
dc = [0, 0, -1, 1]

change = []                                             # 바다로 바꿀 섬의 좌표
for r in range(1, R+1):
    for c in range(1, C+1):
        if jido[r][c] == 'X':                           # 섬인 경우
            cnt = 0                                     # 카운트 초기화
            for i in range(4):                          # 상하좌우 탐색
                if jido[r+dr[i]][c+dc[i]] == '.':       # 바다와 접해있다면 카운트
                    cnt += 1
            else:
                if cnt >= 3:                            # 카운트가 3 이상
                    change.append((r, c))               # 좌표 저장

for r, c in change:                 # 조건에 만족하는 섬을 바다로 변경
    jido[r][c] = '.'
rPosition = []                      # 최종 섬의 행
cPosition = []                      # 최종 섬의 열
for r in range(R+2):
    for c in range(C+2):
        if jido[r][c] == 'X':
            rPosition.append(r)
            cPosition.append(c)

for r in range(min(rPosition), max(rPosition)+1):       # 섬의 행 중 최솟값과 최댓값 사이 탐색
    ans = ''
    for c in range(min(cPosition), max(cPosition)+1):   # 섬의 열 중 최솟값과 최댓감 사이 탐색
        ans += jido[r][c]
    print(ans)

# 방법 2
R, C = map(int, input().split())
jido = [list(input()) for _ in range(R)]

dr = [1, -1, 0, 0]                                              # 상하좌우 델타
dc = [0, 0, -1, 1]

change = []                                                     # 바다로 바꿀 섬의 좌표
for r in range(R):
    for c in range(C):
        if jido[r][c] == 'X':                                   # 섬인 경우
            cnt = 0
            for i in range(4):                                  # 상하좌우 탐색
                if 0 <= r+dr[i] < R and 0 <= c+dc[i] < C:       # 인덱스 안에서 바다와 접해있다면 카운트
                    if jido[r+dr[i]][c+dc[i]] == '.':
                        cnt += 1
                else:                                           # 상하좌우가 인덱스 범위 밖이면 카운트
                    cnt += 1
            else:
                if cnt >= 3:                                    # 바다와 인접 영역이 3 이상이면 좌표 저장
                    change.append((r, c))

for r, c in change:                 # 조건에 만족하는 섬을 바다로 변경
    jido[r][c] = '.'

rPosition = []                      # 최종 섬의 행
cPosition = []                      # 최종 섬의 열
for r in range(R):
    for c in range(C):
        if jido[r][c] == 'X':
            rPosition.append(r)
            cPosition.append(c)

for r in range(min(rPosition), max(rPosition)+1):       # 섬의 행 중 최솟값과 최댓값 사이 탐색
    ans = ''
    for c in range(min(cPosition), max(cPosition)+1):   # 섬의 열 중 최솟값과 최댓값 사이 탐색
        ans += jido[r][c]
    print(ans)