from collections import deque
def bfs(r, c):
    q = deque([])
    q.append((r, c))
    visited[r][c] = 1
    while q:
        v = q.popleft()
        for i in range(8):
            nr = v[0] + dr[i]
            nc = v[1] + dc[i]
            if nr < 0 or nr >= M or nc < 0 or nc >= N:
                continue
            if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))

M, N = map(int, input().split())        # M: 행의 개수, N: 열의 개수
arr = [list(map(int, input().split())) for _ in range(M)]

dr = [-1, 1, 0, 0, -1, -1, 1, 1]    # 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dc = [0, 0, -1, 1, -1, 1, -1, 1]
visited = [[0]*N for _ in range(M)]
ans = 0
for r in range(M):
    for c in range(N):
        if arr[r][c] == 1 and visited[r][c] == 0:
            ans += 1
            bfs(r, c)

print(ans)