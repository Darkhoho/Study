from collections import deque

# 델타
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS
def BFS(Q):
    while Q:
        ty, tx = Q.popleft()
        for n in range(4):
            ny = ty + dy[n]
            nx = tx + dx[n]
            # 만약이 같다면  더이상 진행값하지 않아도 되므로 break
            if (0 <= ny < y and 0 <= nx < x) and (tomato[ny][nx] == 0):
                tomato[ny][nx] = tomato[ty][tx] + 1
                Q.append((ny,nx))


# 입력값 받기
x, y = map(int,input().split())
tomato = [list(map(int,input().split())) for i in range(y)]
result = 0
Q = deque()

# bfs이용해서 번호를 매기는데 큰값이면 먹고 같은값이면 break
for y1 in range(y):
    for x1 in range(x):
        if tomato[y1][x1] == 1:
            Q.append((y1, x1))

BFS(Q)

# 가장 큰 숫자가 횟수라고 생각해도 될까?
result = max(map(max,tomato))

# 만약 0이 있다면 토마토가 만들어 지기 전이니까 result는 -1
for y1 in range(y):
    for x1 in range(x):
        if tomato[y1][x1] == 0:
            result = -1
            break

if result == -1:
    print(result)
else:
    print(result-1)
