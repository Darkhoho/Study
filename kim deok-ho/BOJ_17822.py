from collections import deque
def turn(d, k, cnt):                                    # 원판을 돌리는 함수
    for i in range(cnt):
        turnedPan = [0] * M
        for j in range(M):
            if d:                                       # 반시계 방향
                turnedPan[j-k] = pans[selectedPan[i]][j]
            else:                                       # 시계 방향
                turnedPan[(j+k)%M] = pans[selectedPan[i]][j]
        pans[selectedPan[i]] = turnedPan                # 돌린 원판으로 저장
    bfs()

def bfs():
    result = 0      # 인접한 경우가 있는지 확인하는 변수
    avg = 0         # 평균을 구하기 위한 변수(숫자들의 합)
    numCnt = 0      # 평균을 구하기 위한 숫자의 개수
    check = 0       # 모든 숫자가 제거됐는지 확인하는 변수
    q = deque()
    for r in range(N):
        for c in range(M):
            if pans[r][c] >= 0:
                change = set()
                change.add((r, c))
                q.append((r, c))
                cnt = 0                                                                         # 인접한 숫자의 개수
                while q:
                    r2, c2 = q.popleft()
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr = r2 + dr
                        nc = c2 + dc
                        if nc < 0:                                                              # 양 옆을 봄(인덱스를 넘어가면 계산해서 인덱스 변경)
                            nc = M + nc
                        elif nc >= M:
                            nc = nc % M
                        if nr < 0 or nr >= N or (nr, nc) in change or pans[nr][nc] == -1:
                            continue
                        if pans[r2][c2] == pans[nr][nc]:                                        # 인접 확인 후 위치 저장
                            change.add((nr, nc))
                            q.append((nr, nc))
                            cnt += 1
                if cnt:                                                                         # 인접한 숫자가 있는 경우
                    for r2, c2 in change:
                        pans[r2][c2] = -1                                                       # 인접 숫자들 제거
                    result += 1
                else:                                                                           # 인접 숫자가 없는 경우
                    avg += pans[r][c]
                    numCnt += 1
            elif pans[r][c] == -1:
                check += 1

    if result == 0 and check != N*M:                                                            # 인접 숫자가 하나도 없고 모든 숫자가 제거되지 않은 경우
        avg /= numCnt                                                                           # 평균
        for r in range(N):
            for c in range(M):
                if 0 <= pans[r][c] < avg:                                                       # 조건에 맞게 숫자 변경
                    pans[r][c] += 1
                elif pans[r][c] > avg:
                    pans[r][c] -= 1

    elif check == N*M:
        global isAllRemoved
        isAllRemoved = True

N, M, T = map(int, input().split())     # N: 원판의 개수, M: 원판에 적힌 정수의 개수 , T: 원판 회전시키는 횟수
pans = [list(map(int, input().split())) for _ in range(N)]
isAllRemoved = False
# x의 배수인 원판을 d 방향(시계:0, 반시계:1)으로 k칸 회전
for i in range(T):
    x, d, k = map(int, input().split())
    selectedPan = [j-1 for j in range(x, N+1, x)]
    k = k % M
    cnt = len(selectedPan)
    if not isAllRemoved:
        turn(d, k, cnt)

ans = 0
for r in range(N):
    for c in range(M):
        if pans[r][c] > 0:
            ans += pans[r][c]
print(ans)
