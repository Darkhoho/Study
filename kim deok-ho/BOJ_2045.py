mabang = [list(map(int, input().split())) for _ in range(3)]

zero = []                               # 0인 좌표
target = 0                              # 목표값
total = 0                               # 전체 합

for r in range(3):
    hap1 = 0
    hap2 = 0
    for c in range(3):
        total += mabang[r][c]           # 전체 합

        if mabang[r][c] == 0:           # 행에서 0인 경우
            zero.append((r, c))         # 좌표 저장

        hap1 += mabang[r][c]            # 행의 합
        hap2 += mabang[c][r]            # 열의 합

    big = hap1 if hap1 > hap2 else hap2 # 최댓값을 목표값으로 함
    if target < big:
        target = big

hap1 = 0                                # 대각선의 합
hap2 = 0
for r in range(3):
    for c in range(3):
        if r == c:
            hap1 += mabang[r][c]
        if r+c == 2:
            hap2 += mabang[r][c]
if hap1 == 0 or hap2 == 0:              # 대각선 중  1개라도 0이면
    target = total // 2                 # 목표값 설정
else:                                   # 아니면
    big = hap1 if hap1 > hap2 else hap2 # 최댓값을 목표값으로
    if target < big:
        target = big

for r, c in zero:                       # 행에서 0이 하나만 있으면 채워 넣음
    hap = 0
    cnt = 0
    for i in range(3):
        if mabang[r][i]:
            hap += mabang[r][i]
        else:
            cnt += 1
    if cnt == 1:
        mabang[r][c] = target - hap

for r, c in zero:                       # 열에서 0이 하나만 있으면 채워 넣음
    hap = 0
    cnt = 0
    for i in range(3):
        if mabang[i][c]:
            hap += mabang[i][c]
        else:
            cnt += 1
    if cnt == 1:
        mabang[r][c] = target - hap

for arr in mabang:
    print(*arr)