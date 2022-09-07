from collections import deque

# 델타
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# BFS
def BFS(y, x, color):
    global N
    Q = deque()
    Q.append((y, x))
    visited[y][x] = 1
    while Q:
        qy,qx = Q.popleft()
        for n in range(4):
            ny, nx = qy + dy[n], qx + dx[n]
            if 0 <= nx < N and 0 <= ny < N and ground[ny][nx] == color and visited[ny][nx] == 0:
                if ground[ny][nx] == 'R' or ground[ny][nx] == 'G':
                    ground[ny][nx] = 'M'
                visited[ny][nx] = 1
                Q.append((ny, nx))

# 입력값 받기
N = int(input())
ground = [list(input()) for i in range(N)]
count = miss_count = 0

# 원래 구역이 몇개인지 count하기
visited = [[0]*N for i in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            count += 1
            if ground[y][x] == 'R':
                ground[y][x] = 'M'
                BFS(y,x,'R')
            elif ground[y][x] == 'B':
                BFS(y,x,'B')
            elif ground[y][x] == 'G':
                ground[y][x] = 'M'
                BFS(y,x,'G')

# check를 다했다면 이제 miss로 확인
visited = [[0]*N for i in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            miss_count += 1
            if ground[y][x] == 'M':
                BFS(y,x,'M')
            elif ground[y][x] == 'B':
                BFS(y,x,'B')

print(count, miss_count)
