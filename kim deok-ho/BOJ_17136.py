def attach(r, c, size):                          # 방문 처리
    for nr in range(r, r+size):
        for nc in range(c, c+size):
            paper[nr][nc] = 0

def dettach(r, c, size):                         # 방문 취소
    for nr in range(r, r+size):
        for nc in range(c, c+size):
            paper[nr][nc] = 1

def find(stickCnt, oneCnt):                      # 모든 자리를 붙이는 경우를 찾는 함수(색종이를 붙인 횟수, 남은 붙일 수 있는 자리 개수)
    global ans
    if ans <= stickCnt:                          # 저장된 값 보다 많으면 취소(백트랙킹)
        return
    if oneCnt == 0:                              # 모두 붙이면 최솟값 저장
        ans = min(ans, stickCnt)
        return
    for r in range(10):     
        for c in range(10):
            if paper[r][c] == 1:                 # 붙일 수 있는 위치
                colCnt = 5                       # 최솟값을 찾기 때문에 최댓값으로 먼저 저장
                rowCnt = 0
                for i in range(5):
                    if r + i >= 10 or paper[r+i][c] == 0:
                        break
                    rowCnt += 1
                    tmp = 1
                    j = 1
                    while c + j < 10 and paper[r+i][c+j] and j < 5:
                        tmp += 1
                        j += 1
                    colCnt = min(colCnt, tmp)
                    if rowCnt >= colCnt:                    # 열의 카운트가 행의 카운트 보다 작아지면 종료
                        break
                possible = min(rowCnt, colCnt)              # 붙일 수 있는 크기(행의 카운트, 열의 카운트 중 최솟값), 현재 위치에서 만들 수 있는 최대 정사각형 크기
                for i in range(possible, 0, -1):
                    if size[i] < 5:                         # 사이즈별로 최대 5개 사용 가능
                        attach(r, c, i)
                        size[i] += 1
                        find(stickCnt+1, oneCnt-(i*i))
                        size[i] -= 1
                        dettach(r, c, i)
                return

paper = []               # 종이 정보
oneCnt = 0               # 붙일 수 있는 자리 개수
for _ in range(10):
    data = list(map(int, input().split()))
    paper.append(data)
    oneCnt += data.count(1)

if oneCnt == 0:           
    print(0)
else:
    ans = 100
    size = [0, 0, 0, 0, 0, 0]       # 사이즈별 사용 개수
    find(0, oneCnt)                 
    if ans == 100:                  # 저장된 값이 그대로면 전부 붙일 수 없는 경우
        print(-1)
    else:
        print(ans)