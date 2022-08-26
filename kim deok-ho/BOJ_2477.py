cnt = int(input())
width = []
height = []

maxW = 0
idxW = 0

maxH = 0
idxH = 0
for i in range(6):
    d, l = map(int, input().split())
    if d == 1 or d == 2:    # 가로, 세로 분류, 각 가장 긴 변의 인덱스와 길이 저장
        width.append((i, l))
        if maxW < l:
            maxW = l
            idxW = i
    else:
        height.append((i, l))
        if maxH < l:
            maxH = l
            idxH = i

bigSuqare = maxH*maxW   # 큰 사각형 넓이
smallSquare = 1         # 뺄 사각형 넓이(가장 긴 가로, 세로와 인접하지 않은 가로 세로의 곱)

for i in range(3):
    # 가장 긴 가로가 아니고 가장 긴 세로와 인접하지 않은 가로가 빈 사각형의 가로
    if width[i][0] != idxW and (width[i][0] + 1)%6 != idxH and (width[i][0] - 1)%6 != idxH:
        smallSquare *= width[i][1]
    # 가장 긴 세로가 아니고 가장 긴 가로와 인접하지 않은 세로가 빈 사각형의 세로
    if height[i][0] != idxH and (height[i][0] + 1)%6 != idxW and (height[i][0] - 1)%6 != idxW:
        smallSquare *= height[i][1]

print((bigSuqare-smallSquare)*cnt)