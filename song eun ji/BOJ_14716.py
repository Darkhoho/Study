# 델타
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]

# BFS
def BFS(y1,x1):
    global count
    Q.append((y1,x1))
    while Q:
        ty, tx = Q.pop(0)
        for n in range(8):
            ny = ty + dy[n]
            nx = tx + dx[n]
            # 만약이 같다면  더이상 진행값하지 않아도 되므로 break
            if (0 <= ny < y and 0 <= nx < x) and (paper[ny][nx] == 1):
                paper[ny][nx] = paper[ty][tx] + 1
                Q.append((ny,nx))

    count += 1


# 입력값 받기
y, x = map(int,input().split())
paper = [list(map(int,input().split())) for i in range(y)]
count = 0
Q = []

# bfs이용해서 번호를 매기는데 값이있으면 단어수 세기
for y1 in range(y):
    for x1 in range(x):
        if paper[y1][x1] == 1:
            paper[y1][x1] = 2
            BFS(y1,x1)

print(count)
