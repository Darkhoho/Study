# 방법 1 - 시간 초과
import sys
input = sys.stdin.readline
def dfs(r, c, s, e, hap):
    global ans
    if s == e:
        ans = max(ans, hap)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]:
            continue
        visited[nr][nc] = 1                     # 다음 위치 방문 처리
        dfs(nr, nc, s+1, e, hap+arr[nr][nc])
        visited[nr][nc] = 0                     # 방문 처리 취소

def extra(r, c, s, e, hap):
    global ans
    if s == e:
        ans = max(ans, hap)
    if s == 2:                                  # 현재 2개가 채워졌으므로 현재 위치에서 나머지 두 인접 위치를 찾음
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            extra(r, c, s+1, e, hap + arr[nr][nc])
            visited[nr][nc] = 0
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            extra(r, c, s+1, e, hap + arr[nr][nc])
            visited[nr][nc] = 0

N, M = map(int, input().split())            # N: 세로, 행 M: 가로, 열
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[0]*M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0
for r in range(N):
    for c in range(M):
        visited[r][c] = 1                   # 현재 위치 방문 처리
        dfs(r, c, 1, 4, arr[r][c])          # 한자 철 모양을 제외하고 나머진 도형은 현재 위치에서 dfs로 3번 들어가면 만들어짐
        extra(r, c, 1, 4, arr[r][c])        # 한자 철 모영은 현재 위치에서 dfs로 1번 들어가고 한 위치에서 2번 들어가면 만들어짐
        visited[r][c] = 0                   # 다음 위치에서 활용을 위해 방문 취소

print(ans)

# 방법 2 - 모든 모양 한 번에 확인, 시간 초과
import sys
input = sys.stdin.readline
def dfs(r, c, s, e, hap):
    global ans
    if s == e:
        ans = max(ans, hap)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]:
            continue
        if s == 2:                              # 한자 철 모영은 현재 위치에서 dfs로 1번 들어가고 한 위치에서 2번 들어가면 만들어짐
            visited[nr][nc] = 1
            dfs(r, c, s + 1, e, hap + arr[nr][nc])
            visited[nr][nc] = 0
        visited[nr][nc] = 1                     # 다음 위치 방문 처리
        dfs(nr, nc, s+1, e, hap+arr[nr][nc])
        visited[nr][nc] = 0                     # 방문 처리 취소

N, M = map(int, input().split())            # N: 세로, 행 M: 가로, 열
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[0]*M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0
for r in range(N):
    for c in range(M):
        visited[r][c] = 1                   # 현재 위치 방문 처리
        dfs(r, c, 1, 4, arr[r][c])          # 한자 철 모양을 제외하고 나머진 도형은 현재 위치에서 dfs로 3번 들어가면 만들어짐
        visited[r][c] = 0                   # 다음 위치에서 활용을 위해 방문 취소
print(ans)

# 방법 3 - 백트래킹 적용
import sys
input = sys.stdin.readline
def dfs(r, c, s, e, hap, maxNum):
    global ans
    if hap < ans - maxNum*(e-s):                 # 남은 블록의 개수 곱하기 최댓값을 저장된 값에서 뺀 값보다 현재 값이 작다면 종료
        return
    if s == e:
        ans = max(ans, hap)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]:
            continue
        if s == 2:                              # 한자 철 모영은 현재 위치에서 dfs로 1번 들어가고 한 위치에서 2번 들어가면 만들어짐
            visited[nr][nc] = 1
            dfs(r, c, s + 1, e, hap + arr[nr][nc], maxNum)
            visited[nr][nc] = 0
        visited[nr][nc] = 1                     # 다음 위치 방문 처리
        dfs(nr, nc, s+1, e, hap+arr[nr][nc], maxNum)
        visited[nr][nc] = 0                     # 방문 처리 취소

N, M = map(int, input().split())            # N: 세로, 행 M: 가로, 열
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[0]*M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
maxNum = 0
for r in range(N):
    rowMax = max(arr[r])
    if maxNum < rowMax:
        maxNum = rowMax

ans = 0
for r in range(N):
    for c in range(M):
        visited[r][c] = 1                   # 현재 위치 방문 처리
        dfs(r, c, 1, 4, arr[r][c], maxNum)  # 한자 철 모양을 제외하고 나머진 도형은 현재 위치에서 dfs로 3번 들어가면 만들어짐
        visited[r][c] = 0                   # 다음 위치에서 활용을 위해 방문 취소
print(ans)