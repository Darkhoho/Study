# N극은0 S극은1
# 톱니바퀴는 4개
# 회전수
# 회전방법
# 12시에 N극이 있으면 0점 S극이 있으면(1,2,4,8)
# 시계 1 반시계 -1

# 돌아라!
# 원형큐 사용한거 처럼 사용할까?
# 그냥 돌려버리자
def wheel(N, K):
    de_wheel = [0]*8
    if K == 1:
        for i in range(8):
            de_wheel[i] = wheels[N][i-1]
        wheels[N] = de_wheel
    elif K == -1:
        for i in range(8):
            de_wheel[i-1] = wheels[N][i]
        wheels[N] = de_wheel
    return

# 계산에 넣자
# 아,,,, 근데 순서는 어떻게 확인하지,,,, 1234순이 아닐텐데
# 일단 들어오자마자 비교하고 회전시키자
def calcul(N, K):
    # 처음인지 먼저 확인하기
    if N == 1:
        if wheels[N-1][2] != wheels[N][6]:
            if go[N-1] != 0:
                if K == 1:
                    go[N] = -1
                elif K == -1:
                    go[N] = 1

    # 중간인지 확인하기
    if N == 2 or N == 3:
        if wheels[N - 1][2] != wheels[N][6]:
            if go[N-1] != 0:
                if K == 1:
                    go[N] = -1
                elif K == -1:
                    go[N] = 1

        if wheels[N - 1][6] != wheels[N - 2][2]:
            if go[N-1] != 0:
                if K == 1:
                    go[N-2] = -1
                elif K == -1:
                    go[N-2] = 1

    # 끝인지 확인하기
    if N == 4:
        if wheels[N - 1][6] != wheels[N - 2][2]:
            if go[N-1] != 0:
                if K == 1:
                    go[N-2] = -1
                elif K == -1:
                    go[N-2] = 1


wheels = [list(map(int,input())) for i in range(4)]
num = [[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,3,2,1]]

for i in range(int(input())):
    N, K = map(int,input().split())
    go = [0] * 4
    go[N-1] = K

    # 네개다 돌려주기
    for c in range(4):
        calcul(num[N-1][c],go[num[N-1][c]-1])
    for c in range(4):
        wheel(c,go[c])

# 점수계산하자
score = [1,2,4,8]
result = 0

for i in range(4):
    if wheels[i][0] == 1:
        result += score[i]
print(result)
