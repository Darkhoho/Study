def check(cnt, num):
    if cnt == 3:                        # 장애물 3개 설치한 경우
        for i in range(num):
            r, c = students[i]          # 학생의 위치에서 선생님이 보이는지 확인 
            for j in range(4):
                for k in range(1, N):   # 한 방향으로 계속 이동
                    nr = r + dr[j]*k
                    nc = c + dc[j]*k
                    if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] == 'O' or arr[nr][nc] == 'S':
                        break
                    if arr[nr][nc] == 'T':
                        return False    # 보인다면 False
        return True                     # 한 번도 선생님이 안 보이면 True
    else:
        for r in range(N):
            for c in range(N):
                if arr[r][c] == 'X':        # 장애물 설치
                    arr[r][c] = 'O'
                    if check(cnt+1, num):   # 다음 장애물을 설치하거나 3개를 다 설치했으면 학생 위치에서 확인
                        return True         # 선생님을 모두 피했으면 True
                    arr[r][c] = 'X'         # 다른 곳에 장애물 설치를 위해 장애물 제거
    return False

N = int(input())
arr = [input().split() for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


students = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 'S':
            students.append((r, c))     # 학생들 위치 저장
stdNum = len(students)

if check(0, stdNum):
    print('YES')
else:
    print('NO')