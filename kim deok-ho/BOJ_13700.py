# 방법 1 - bfs
from collections import deque
def bfs(S, D, N, F, B):
    visited = [0]*(N+1)
    q = deque()
    visited[S] = 1
    q.append(S)
    while q:
        v = q.popleft()
        frontPosition = v + F
        backPosition = v - B
        if frontPosition <= N and frontPosition not in police and visited[frontPosition] == 0:
            visited[frontPosition] = visited[v] + 1
            q.append(frontPosition)
        if backPosition >= 1 and backPosition not in police and visited[backPosition] == 0:
            visited[backPosition] = visited[v] + 1
            q.append(backPosition)
        if visited[D]:
            return visited[D]-1
    return 'BUG FOUND'

# 마포구 건물의 개수 N, 털린 금은방 S, 
# 대도 X의 집 D, 앞으로 한 번에 달릴 수 있는 건물 수 F, 
# 뒤로 한 번에 달릴 수 있는 건물 수 B, 마포구 경찰서의 개수 K
N, S, D, F, B, K = map(int, input().split())
if K > 0:
    police = list(map(int, input().split()))
else:
    police = []
print(bfs(S, D, N, F, B))

# 방법 2 - dfs
