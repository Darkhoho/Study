# 입력값 받기
R, C = map(int,input().split())
ground = [list(input()) for i in range(R)]

# 델타 이용
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 땅 확인하기
s1 = [] # 살아있는땅 입력할 값
s2 = []
s3 = [] # 죽을 땅 입력할 값
s4 = []
for y in range(R):
    for x in range(C):
        count = 0
        if ground[y][x] == 'X':
            for k in range(4): # 주변에 땅이 2군데 이상이면 값을 저장하기
                j = x + dx[k]
                k = y + dy[k]
                if (0 <= j < C and 0 <= k < R) and ground[k][j] == 'X':
                    count += 1
            if count > 1:
                s1.append(y)
                s2.append(x)
            else:
                s3.append(y)
                s4.append(x)

# 땅에서 바다로 바뀐부분 바꾸기
for i in range(len(s3)):
    ground[s3[i]][s4[i]] = '.'

# 있는 자리에 맞추어서 지도 나타내기
for y in range(min(s1),max(s1)+1):
    for x in range(min(s2),max(s2)+1):
        print(ground[y][x], end=' ')
    print()