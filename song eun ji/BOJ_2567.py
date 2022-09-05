# 일단 0으로 다 만들어 두기
paper = [[0]*101 for i in range(101)]

y1_max = x1_max = 0
# 종이 넓이 나타내주기
for p in range(int(input())):
    y1, x1 = map(int,input().split())
    for y in range(y1, y1+10):
        for x in range(x1, x1+10):
            paper[y][x] = 1

# 처음 좌표를 잡고 둘레를 따라가면서 0이 있으면 둘레
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 0
for y in range(101):
    for x in range(101):
        if paper[y][x] == 1:
            for n in range(4):
                nx = x + dx[n]
                ny = y + dy[n]
                if (0 <= nx < 101 and 0 <= ny < 101) and paper[ny][nx] == 0: # 둘레인경우
                    count += 1


print(count)
