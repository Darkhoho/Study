from collections import deque
def bfs(r, c, N, M):
    visited = [[0]*M for _ in range(N)]
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    result = 0
    while q:
        v = q.popleft()
        for i in range(4):
            nr = v[0] + dr[i]
            nc = v[1] + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]:
                continue
            if arr[nr][nc] == 'L':
                visited[nr][nc] = visited[v[0]][v[1]] + 1
                q.append((nr, nc))
                result = visited[nr][nc]-1
    return result
        
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'L':                # 육지이면 현재 위치에서 최단거리로 가장 먼 곳을 찾음
            result = bfs(r, c, N, M)
            if ans < result:
                ans = result
print(ans)