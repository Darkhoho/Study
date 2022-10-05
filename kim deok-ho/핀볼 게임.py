block = {1: (1, 3, 0, 2),                               # 방향 전환
         2: (3, 0, 1, 2),
         3: (2, 0, 3, 1),
         4: (1, 2, 3, 0),
         5: (1, 0, 3, 2)}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, d):                                       # 충돌 횟수
    sr, sc = r, c
    cnt = 0
    while True:
        r += dr[d]
        c += dc[d]
        if r < 0 or r >= N or c < 0 or c >= N or jido[r][c] == 5:       # 진행 방향 180도로 전환되면 종료
            return cnt*2 + 1                            # 지금까지 저장된 값 * 2 + 1
        
        elif 1 <= jido[r][c] < 5:                       # 블록인 경우
            nd = block[jido[r][c]][d]                   # 방향을 바꿈
            if d in (0, 1) and nd in (0, 1):
                return cnt*2 + 1
            elif d in (2, 3) and nd in (2, 3):          # 만약 방향이 반대로 된다면 원래 위치로 돌아가므로 종료
                return cnt*2 + 1
            else:                                       # 방향 바꾸고 카운트
                cnt += 1
                d = nd
                
        elif 6 <= jido[r][c] <= 10:                     # 웜홀
            hole = jido[r][c]-6
            for i in range(2):
                if (r, c) != wormhole[hole][i]:
                    r, c = wormhole[hole][i]            # 이동
                    break
                    
        elif jido[r][c] == -1:                          # 블랙홀
            return cnt
        
        elif r == sr and c == sc:                       # 원위치
            return cnt


for case in range(1, int(input())+1):
    N = int(input())
    jido = [list(map(int, input().split())) for _ in range(N)]

    wormhole = [[] for _ in range(5)]           # 웜홀 위치

    for r in range(N):
        for c in range(N):
            if jido[r][c] >= 6:
                wormhole[jido[r][c]-6].append((r, c))

    ans = 0
    for r in range(N):
        for c in range(N):
            if jido[r][c] == 0:
                for i in range(4):
                    ans = max(ans, dfs(r, c, i))
    print(f'#{case} {ans}')