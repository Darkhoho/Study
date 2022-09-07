# 델타
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 학생을 찾자
def find_S(y,x):
    global  N
    for n in range(4):
        ny = y + dy[n]
        nx = x + dx[n]
        while 0 <= ny < N and 0 <= nx < N and ground[ny][nx] != 'O':
            # 찾았다!
            if ground[ny][nx] == 'S':
                return -1
            else:
                ny += dy[n]
                nx += dx[n]
    # 못찾았다!
    return 1

# 벽을 하나하나 세워보자,,,,
def wall(w):
    global N, count, result

    # 만약에 벽을 3개 다 설치했다면 선생님이 학생을 찾을 수 있는지 확인하기
    if count == 3:
        not_find = 0
        for ty, tx in teacher:
            # 찾지 못했다면?
            find = find_S(ty,tx)
            if find == 1:
                not_find += 1
            else:
                break

        # 선생님과 찾지 못한 수가 같다면? 학생이 잘 숨은거
        if not_find == len(teacher):
            result = 'YES'
        return

    # 벽이 3개다 설치를 안했을시
    for wy in range(N):
        for wx in range(N):
            # 벽이 아니라면 벽을 설치후 다음거에도 해보기
            if ground[wy][wx] == 'X':
                ground[wy][wx] = 'O'
                count += 1
                wall(count)

                # 벽이 소용이 없다면 벽을 없애고 count 1개 빼주기
                ground[wy][wx] = 'X'
                count -= 1


# 입력값 받기
N = int(input())
ground = [list(map(str,input().split())) for i in range(N)]
teacher = []
count = 0
result = 'NO'

for y in range(N):
    for x in range(N):
        # 선생님 위치 정해서 'X'있는데에 다 넣어서 확인하자,,,,,
        if ground[y][x] == 'T':
            teacher.append((y,x))

wall(0)
print(result)