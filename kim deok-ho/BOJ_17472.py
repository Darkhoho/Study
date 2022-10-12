from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def islandNum(r, c, num):                                   # 섬들에 번호 설정(2부터)하는 함수
    q = deque()
    q.append((r, c))
    jido[r][c] = num
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if jido[nr][nc] == 1:
                q.append((nr, nc))
                jido[nr][nc] = num

def findEdge(r, c):                                        # 간선 찾는 함수
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M or jido[nr][nc]:
            continue
        cnt = 0
        while 0 <= nr < N and 0 <= nc < M and jido[nr][nc] == 0:
            cnt += 1
            nr = nr + dr[d]
            nc = nc + dc[d]
        if 0 <= nr < N and 0 <= nc < M and jido[r][c] != jido[nr][nc] and cnt > 1:
            E.add((jido[r][c], jido[nr][nc], cnt))

def findSet(x):
    while x != disjoint[x]:
        x = disjoint[x]
    return x

N, M = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
num = 1
for r in range(N):
    for c in range(M):
        if jido[r][c] == 1:
            num += 1
            islandNum(r, c, num)

E = set()               
for r in range(N):
    for c in range(M):
        if jido[r][c] != 0:
            findEdge(r, c)
E = sorted(list(E), key=lambda x:x[2])          # 간선을 거리를 기준으로 오름차순 정렬
disjoint = list(range(num+1))

ans = 0
for v, w, weight in E:                          # kruskal 활용
    v = findSet(v)
    w = findSet(w)
    if v != w:
        disjoint[v] = w
        ans += weight
        num -= 1
        if num == 2:
            print(ans)
            break
else:
    print(-1)