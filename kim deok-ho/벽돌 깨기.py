from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(cnt, blocks):                              # 공을 쏘는 함수
    global ans
    if ans == 0:                                   # 0이 되면 최솟값이 확정된 것이므로 종료
        return
    if cnt == 0:                                   # 공을 다 쏘면 최솟값 저장
        left = notZero(blocks)
        ans = min(ans, left)
        return
    for c in range(W):
        for r in range(H):
            if blocks[r][c] >= 1:
                nextBlocks = bfs(r, c, blocks)
                dfs(cnt-1, nextBlocks)
                break

def bfs(r, c, blocks):                              # 벽돌이 부숴지는 함수
    visited = [[1]*W for _ in range(H)]             # 벽돌이 없어지면 0
    q = deque()
    q.append((r, c))
    visited[r][c] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            for j in range(blocks[r][c]):
                nr = r + dr[i] * j
                nc = c + dc[i] * j
                if nr < 0 or nr >= H or nc < 0 or nc >= W or blocks[nr][nc] == 0:
                    continue
                if visited[nr][nc]:
                    visited[nr][nc] = 0
                    q.append((nr, nc))
    nextBlocks = [[0]*W for _ in range(H)]          # 모두 부숴진 후 결과
    noOver = set()                                  # 더 이상 확인하지 않아도 되는 열
    for r in range(H-1, -1, -1):                    # 거꾸로 확인
        for c in range(W-1, -1, -1):
            if c in noOver:
                continue
            if visited[r][c]:                       # 벽돌이 남아있으면 저장
                nextBlocks[r][c] = blocks[r][c]
            else:
                for nr in range(r, -1, -1):         # 벽돌이 없으면
                    if visited[nr][c]:              # 행을 올려가며 남아있으면 교체 후 저장
                        visited[r][c], visited[nr][c] = visited[nr][c], visited[r][c]
                        nextBlocks[r][c] = blocks[nr][c]
                        break
                else:                               # 남은 벽돌이 없으면 해당 열을 셋에 저장
                    noOver.add(c)
    return nextBlocks

def notZero(blocks):                                # 남은 벽돌 카운트 함수
    left = 0
    for r in range(H):
        for c in range(W):
            if blocks[r][c]:
                left += 1
    return left

for case in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]
    ans = W * H
    dfs(N, blocks)
    if ans == W*H:                                   # 초기값 그대로 이면 벽돌이 처음부터 없었던 것
        ans = 0
    print(f'#{case} {ans}')