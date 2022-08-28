def dfs(r, c, color):
    global nth
    nth += 1
    visited[r][c] = 1           # 방문 처리
    war[r][c] = 0               # 지도 변경(다시 확인하지 않기 위해)
    for i in range(4):          
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= M or nc < 0 or nc >= N:
            continue
        if war[nr][nc] == color:    # 같은 색이면 다음 인접 확인
            dfs(nr, nc, color)
    return

N, M = map(int, input().split())
war = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

black = 0
white = 0
for r in range(M):
    for c in range(N):
        if war[r][c] == 'W':
            nth = 0
            dfs(r, c, 'W')
            white += nth**2
        elif war[r][c] == 'B':
            nth = 0
            dfs(r, c, 'B')
            black += nth**2

print(white, black)