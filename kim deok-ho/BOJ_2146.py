from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(r, c, check):
    q = deque()
    q.append((r, c))
    arr[r][c] = check
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if arr[nr][nc] == 1:
                arr[nr][nc] = check
                q.append((nr, nc))
            if arr[nr][nc] == 0:
                checkPosition.add((nr, nc))

def find(r, c):
    global ans
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[nr][nc] != 0:
            near = arr[nr][nc]
            break
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        if ans <= visited[r][c]:
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:
                continue
            if arr[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
            elif arr[nr][nc] != near:
                ans = min(ans, visited[r][c])
                return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
check = 2
checkPosition = set()
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            bfs(r, c, check)
            check += 1
ans = N*N
for r, c in checkPosition:
    find(r, c)
print(ans)