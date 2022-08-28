from collections import deque

def bfs():
    dr = [-1, 1, 0, 0]                      
    dc = [0, 0, -1, 1]
    visited = [[0]*M for _ in range(N)]                            # 큐에 저장됨을 확인
    q = deque([])                                                  # 방문할 곳을 저장할 큐
    for r in range(N):
        for c in range(M):
            if tomato[r][c] == 1:
                q.append((r, c))                                   # 큐에 저장 후 큐 저장 처리
                visited[r][c] = 1
            elif tomato[r][c] == -1:                               # 비어있는 곳도 큐에 저장된 것으로 처리
                visited[r][c] = 1               
    while q:
        v = q.popleft()                                    
        for i in range(4):                                         # 사방을 확인
            nr = v[0] + dr[i]
            nc = v[1] + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if tomato[nr][nc] == 0 and visited[nr][nc] == 0:      # 토마토가 익지 않고 큐에 저장된 적이 없는 경우
                q.append((nr, nc))                                # 처리
                visited[nr][nc] = visited[v[0]][v[1]] + 1
    ans = 0
    for r in range(N):                                            
        if min(visited[r]) == 0:                                  # 최솟값이 0이면 익지 않은 토마토가 있는 것
            return -1
        if ans < max(visited[r]):
            ans = max(visited[r])
    return ans-1

M, N = map(int, input().split())                                # M: 열의 개수, N: 행의 개수
tomato = [list(map(int, input().split())) for _ in range(N)]
print(bfs())