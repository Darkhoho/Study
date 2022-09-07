from collections import deque

# 델타
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS로?
def BFS(y,x):
    global N, L, R
    Q = deque()
    Q.append((y,x))
    visited[y][x] = 1
    while Q:
        qy, qx = Q.popleft()
        for n in range(4):
            nx = qx + dx[n]
            ny = qy + dy[n]
            # 만약에 길이에 들어오고 방문하지 않았고, 차이가 L과 R사이라면?
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
                if L <= abs(person[ny][nx] - person[qy][qx]) <= R:
                    visited[ny][nx] = 1
                    Q.append((ny,nx))
                    border.append((ny, nx))

# 입력값 받기
N, L, R = map(int,input().split())
person = [list(map(int,input().split())) for i in range(N)]
day = 0

while True:
    visited = [[0] * N for i in range(N)]
    more = 0
    # 오키 하루는 짰어,,, 그래서? while로?
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:
                border = []
                country_person = 0
                border.append((y,x))
                BFS(y,x)
                # 만약 1이라면 굳이?
                if len(border) != 1:
                    more = 1
                    for y1, x1 in border:
                        country_person += person[y1][x1]
                    move_person = country_person // len(border)
                    for y1, x1 in border:
                        person[y1][x1] = move_person
    if more == 1:
        day += 1
    else:
        break

print(day)
