# 방법1 - 파이썬 시간 초과, pypy 통과
from collections import deque
def bfs(r, c):
    global hap
    cnt = 1                                                     # 본인 포함해서 1로 시작
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    connected.append((r, c))                                    # 현재 위치 추가
    while q:
        r1, c1 = q.popleft()
        for i in range(4):
            nr = r1 + dr[i]
            nc = c1 + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:
                continue
            if L <= abs(arr[r1][c1] - arr[nr][nc]) <= R: 
                cnt += 1                                        # 조건 만족하는 국가 카운트
                hap += arr[nr][nc]
                visited[nr][nc] = 1
                q.append((nr, nc))
                connected.append((nr, nc))                      # 조건 만족 국가 위치 추가
    return cnt

N, L, R = map(int, input().split())                             # N: 배열 크기, L: 최소 차이, R: 최대 차이

arr = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

i = 0                                                           # 발생 일수
change = 1                                                      # 인구 이동이 일어난 횟수(반복 시작을 위해 1로 시작)
while change:
    change = 0                                                  # 인구 이동 횟수 초기화
    visited = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            connected = []                                      # 조건 만족 국가 위치
            hap = arr[r][c]                                     # 조건 만족 국가의 인구 합
            cnt = bfs(r, c)
            if cnt > 1:                                         # 조건 만족 국가가 2 이상이면 이동 발생
                change += 1
                for j in range(cnt):                            # 해당 위치 전부 인구 수정
                    arr[connected[j][0]][connected[j][1]] = hap//cnt
    if change:                                                  # 이동이 일어났으므로 하루 지남
        i += 1

print(i)