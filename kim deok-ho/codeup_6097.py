# 높이와 너비
h, w = map(int, input().split())
# 스틱 개수
stickNum = int(input())
# 스틱 정보
stickData = []
# 입력 받아서 정보 리스트에 리스트로 저장
for i in range(stickNum):
    stickData.append(list(map(int, input().split())))
# 스틱 정보2
stickData2 = []
# 스틱 개수만큼 반복
for i in range(stickNum):
    for j in range(stickData[i][0]):
        # 스틱의 배치를 보고 가로면 가로로 좌표를 세로면 세로로 좌표를 저장
        if stickData[i][1] == 0:
            stickData2.append([stickData[i][2], stickData[i][3]+j])
        else:
            stickData2.append([stickData[i][2]+j, stickData[i][3]])

# 판을 모두 0을 가진 리스트로 만든다.
pan = [[0]*w for i in range(h)]
# 저장한 정보에 해당하는 좌표를 1로 바꾼다.
for point in stickData2:
    pan[point[0]-1][point[1]-1] = 1

for i in range(h):
    for j in range(w):
        print(pan[i][j], end=' ')
    print()