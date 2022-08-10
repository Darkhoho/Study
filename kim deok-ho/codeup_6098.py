# 10*10 미로 상자 리스트 만들기
maze = []
for _ in range(10):
    maze.append(list(map(int, input().split())))

# 인덱스 시작 값
n=1
m=1
while True:
    # 현재 위치가 0이면 9로 만든다.
    if maze[n][m] == 0:
        maze[n][m] = 9
        # 오른쪽에 길이 있으면 오르쪽으로 움직인다.
        if maze[n][m+1] == 0 or maze[n][m+1] == 2:
            m += 1
        # 오른쪽이 막혀있고 아래도 막혀있으면 그 자리에 있는다.
        elif maze[n][m+1] == 1 and maze[n+1][m] == 1:
            break
        # 오른쪽만 막혔으면 아래로 내려간다.
        else:
            n += 1
    # 현재 위치에 먹이가 있으면 먹고 9로 만든 뒤 그 자리에 있는다.
    else:
        maze[n][m] = 9
        break
    

for num1 in range(10):
    for num2 in range(10):
        print(maze[num1][num2], end=' ')
    print()
