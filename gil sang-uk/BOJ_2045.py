import sys;input=sys.stdin.readline
# 9 9 0 마방진 특성 한열의 합 = 기준합
# 9 0 9 마방진의 모든 숫자를더하면 = 기준합*3
# 0 9 9 마방진의 다른 숫자의 합 = 기준합 *3 - 기준합 = 기준합*2//2

# 9 9 9
# 9 9 9
# 9 9 9
# 0이 있는지 검사
def no_z(li):
    for i in range(3):
        if li[i] == 0:
            return 0
    return sum(li) #기준합
# 기준 합으로 채우기
def magic_square(res):
    # 열 먼저 채우기
    for i in range(3):
        # 0이 두개있는 경우
        if sum(li[i]) == max(li[i]): # 9 0 0 /  9 9
            continue
        for j in range(3):
            if li[i][j] == 0:
                li[i][j] = res - sum(li[i]) # 9 9 9  27-18= 9
    # 행 채우기
    for i in range(3):
        for j in range(3):
            if li[j][i] == 0:
                li[j][i] = res - (li[0][i] + li[1][i] + li[2][i])

def solve():
    # 0이 없는 곳으로 기준합 정하기
    tmp = []
    for i in range(3):
        tmp += [no_z(li[i]), no_z(c_li[i])]
    tmp += [no_z(l_dia), no_z(r_dia)]
    res = max(tmp)
    # 기준합 있는 경우
    if res:
        magic_square(res)
    # 모든 줄에 0이 있다면 다른 부분의 합//2가 기준합이 됨 (대각선의 합과 같아짐)
    else:
        res = 0
        for r in range(3):
            for c in range(3):
                res += li[r][c]
        magic_square(res//2)
            

li = [(list(map(int, input().split()))) for _ in range(3)]
c_li = list(zip(*li))
l_dia,r_dia = [], []
for i in range(3):
    l_dia.append(li[i][i])
    r_dia.append(li[2-i][i])
solve()
for i in range(3):
    print(*li[i])