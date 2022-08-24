def rcCheck(r, c):                  # 행, 열 확인
    result = 0
    for i in range(5):
        if bingo[r][i] != 0:
            break
    else:
        result += 1
    for i in range(5):
        if bingo[i][c] != 0:
            break
    else:
        result += 1
    return result

def cross1():                       # 왼쪽-오른쪽 아래 대각선
    for r in range(5):
        for c in range(5):
            if r == c and bingo[r][c] != 0:
                return 0
    return 1

def cross2():                       # 오른쪽-왼쪽 아래 대각선
    for r in range(5):
        for c in range(5):
            if r+c == 4 and bingo[r][c] != 0:
                return 0
    return 1

def totalCheck(r, c):               # 빙고 모두 확인(행, 열, 대각선)
    result = 0
    result += rcCheck(r, c)         # 행, 열 빙고 개수만큼 더하기
    if r == 2 and c == 2:           # 가운데 위치면 대각선 2개 다 보고 개수 더하기
        if cross1():
            result += 1
        elif cross2():
            result += 1
    elif r + c == 4:                # 오른쪽-왼쪽 아래 대각선 확인
        if cross2():
            result += 1
    elif r == c:                    # 왼쪽-오른쪽 아래 대각선 확인
        if cross1():
            result += 1
    return result

def callNum():
    ans = 0                                         # 부른 횟수
    cnt = 0                                         # 빙고 개수
    for _ in range(5):
        nums = list(map(int, input().split()))
        for num in nums:
            ans += 1
            for r in range(5):
                for c in range(5):
                    if bingo[r][c] == num:
                        bingo[r][c] = 0
                        cnt += totalCheck(r, c)    # 빙고 개수 더하기
                        if cnt >= 3:                
                            return ans

bingo = [list(map(int, input().split())) for _ in range(5)]
print(callNum())





