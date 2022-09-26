from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    result = set()
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            if arr[nr][nc] == 1:
                result.add((nr, nc))
                continue
            q.append((nr, nc))
    return result

N, M = map(int, input().split())        # N: 세로, M: 가로
passList = [0]*M
arr = [list(map(int, input().split())) for _ in range(N)]

ans1 = 0
while True:
    for r in range(N):
        if arr[r] == passList:
            continue
        for c in range(M):
            if arr[r][c] == 1:
                ans1 += 1
                visited = [[0]*M for _ in range(N)]
                changeList = bfs(r-1, c)
                ans2 = 0
                for r, c in changeList:
                    arr[r][c] = 0
                    ans2 += 1
                break
    else:
        print(ans1)
        print(ans2)
        break

