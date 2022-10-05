def findMax(r, c, cnt, left):
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:
            continue
        if jido[nr][nc] < jido[r][c]:                       # 높이가 낮으면
            visited[nr][nc] = 1
            findMax(nr, nc, cnt+1, left)
            visited[nr][nc] = 0
        elif left:                                          # 공사가 가능하면
            gap = jido[nr][nc] - jido[r][c]
            if gap < K:                                     # 공사해서 높이가 작아지면
                jido[nr][nc] -= gap+1
                visited[nr][nc] = 1
                findMax(nr, nc, cnt + 1, 0)
                jido[nr][nc] += gap+1
                visited[nr][nc] = 0
    global ans
    ans = max(ans, cnt)

for case in range(1, int(input())+1):
    N, K = map(int, input().split())
    jido = [[0]*N for _ in range(N)]
    pointVal = 0                                # 가장 높은 높이
    for i in range(N):
        data = list(map(int, input().split()))
        jido[i] = data
        pointVal = max(pointVal, max(data))

    starts = set()                              # 가장 높은 봉우리
    for r in range(N):
        for c in range(N):
            if pointVal == jido[r][c]:
                starts.add((r, c))

    ans = 0
    for r, c in starts:
        visited = [[0]*N for _ in range(N)]
        visited[r][c] = 1
        findMax(r, c, 1, 1)
        visited[r][c] = 0
    print(f'#{case} {ans}')