def checkPostion(r, c):                         # 공기청정기 작동 후 위치 확인 함수
    if c == C-1 and r not in {0, R-1}:          # 마지막 열에 위치하면서 첫 행과 끝 행이 아닌 경우
        if r <= machine[0]:                     # 공기 청정기 상단
            r -= 1
        elif r >= machine[1]:                   # 공기 청정기 하단
            r += 1
    elif c == 0:                                # 가장 앞 열에 위치
        if r < machine[0]:                      # 공기청정기 상단
            r += 1
        elif r > machine[1]:                    # 공기청정기 하단
            r -= 1
    elif r in {0, R-1}:                         # 첫 행과 마지막 행에 위치한 경우
        c -= 1
    elif r in machine:                          # 공기청정기가 있는 행에 위치한 경우
        c += 1
    return r, c


def airFresh():
    newRoom = [[0]*C for _ in range(R)]                                    # 새로운 방 정보
    newPostion = set()                                                     # 새로운 먼지 위치
    for r, c in dustPosition:
        movedDust = room[r][c]//5                                          # 움직이는 먼지량
        moveCnt = 0                                                        # 움직인 횟수

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= R or nc < 0 or nc >= C or (nr in machine and nc == 0):
                continue
            moveCnt += 1
            nr, nc = checkPostion(nr, nc)
            if nr in machine and nc == 0:                                # 공기청정기에 들어가는 경우
                continue
            else:
                newRoom[nr][nc] += movedDust
                newPostion.add((nr, nc))

        leftDust = room[r][c] - movedDust*moveCnt                        # 남은 먼지
        r, c = checkPostion(r, c)
        if r in machine and c == 0:                                      # 공기청정기에 들어가는 경우
            continue
        else:
            newRoom[r][c] += leftDust
            newPostion.add((r, c))

    return newRoom, newPostion

# 방법
# 1. 먼지 위치 저장
# 2. 공청기의 행 위치 저장
# 3. 새로운 먼지 위치 정보를 저장할 리스트와 셋 초기화
# 4. 현재 먼지를 확산시키고 공청기 작동 후 위치로 옮긴 후 리스트와 셋에 저장
# 5. 새로 만든 리스트와 셋을 이전에 만들었던 리스트와 셋에 덮어씌움
# 6. T만큼 반복

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

dustPosition = set()
machine = []
for r in range(R):
    if room[r][0] == -1:
        machine.append(r)
    for c in range(C):
        if room[r][c] > 0:
            dustPosition.add((r, c))

for i in range(T):
    room, dustPosition = airFresh()

ans = 0
for i in range(R):
    ans += sum(room[i])
print(ans)