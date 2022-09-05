from collections import deque
def bfs(arr, r, c, color):
    arr[r][c] = 1
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc]:
                continue
            if colors[nr][nc] in color:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))
    return

N = int(input())

colors = [input() for _ in range(N)]
visited1 = [[0]*N for _ in range(N)]                # 정상
visited2 = [[0]*N for _ in range(N)]                # 색약

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

normalCnt = 0                                               # 정상의 눈에서 보이는 그룹 수
abnormalCnt = 0                                             # 색약의 눈에서 보이는 그룹 수
for r in range(N):
    for c in range(N):
        if colors[r][c] == 'B' and visited1[r][c] == 0:     # 파랑은 색약과 정상 모두 같이 보임
            normalCnt += 1
            abnormalCnt += 1
            bfs(visited1, r, c, ['B'])
            continue
        elif colors[r][c] != 'B':                           # 파랑이 아닌 경우
            if visited1[r][c] == 0:                         # 정상은 녹색과 적색을 따로 취급
                normalCnt += 1
                bfs(visited1, r, c, [colors[r][c]])
            if visited2[r][c] == 0:                         # 색약은 녹색과 적색을 같은 것으로 취급
                abnormalCnt += 1
                bfs(visited2, r, c, ['R', 'G'])

print(normalCnt, abnormalCnt)