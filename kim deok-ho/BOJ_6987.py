def match(t, cnt, lst):                 # 6C2개의 모든 경기를 찾음
    if cnt == 2:
        games.append((lst[0], lst[1]))
        return
    if t == N:
        return
    match(t+1, cnt+1, lst + [t])
    match(t+1, cnt, lst)

def play(cnt):
    if cnt == 15:
        # 승리, 무승부, 패배 모두 0이 된다면 가능한 경우
        if sum(win) == 0 and sum(draw) == 0 and sum(lose) == 0:
            return 1
        return 0

    t1, t2 = games[cnt]                 # 현재 경기하는 두 팀을 가져오기
    if win[t1] > 0 and lose[t2] > 0:    # t1이 이기는 경우
        win[t1] -= 1
        lose[t2] -= 1
        if play(cnt+1):
            return 1
        win[t1] += 1
        lose[t2] += 1

    if draw[t1] > 0 and draw[t2] > 0:   # t1이 비기는 경우
        draw[t1] -= 1
        draw[t2] -= 1
        if play(cnt + 1):
            return 1
        draw[t1] += 1
        draw[t2] += 1

    if lose[t1] > 0 and win[t2] > 0:    # t1이 지는 경우
        lose[t1] -= 1
        win[t2] -= 1
        if play(cnt + 1):
            return 1
        lose[t1] += 1
        win[t2] += 1

    return 0
N = 6
teams = [i for i in range(6)]
games = []                              # 6C2 조합 찾기(모든 경기)
match(0, 0, [])

datas = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    win , draw, lose = [], [], []       # 각 팀 번호를 인덱스로 승리, 무승부, 패배 횟수 저장
    for j in range(6):
        win.append(datas[i][j*3])
        draw.append(datas[i][j*3+1])
        lose.append(datas[i][j*3+2])
    print(play(0), end=' ')