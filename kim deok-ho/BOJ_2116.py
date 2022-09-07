import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
updown = [5, 3, 4, 1, 2, 0]
ans = 0
def findMax(s, N, t, fs):                             # s: 현재 주사위, N: 마지막 주사위, t: 윗 면, b: 아랫 면
    global ans
    if fs < ans-(N-s)*6:
        return
    if s == N:                                           # 마지막 주사위까지 다 쌓으면 비교
        if ans < fs:
            ans = fs
        return
    b = t                                                # 아래를 위 숫자로 두기
    for i in range(6):                                   # 아래가 정해지면 위를 설정
        if b == dices[s][i]:
            t = dices[s][updown[i]]
            break
    num = 0
    for i in range(6):                                  # 아래, 위를 제외하고 돌리면서 앞 확인
        if b == dices[s][i] or t == dices[s][i]:
            continue
        if num < dices[s][i]:
            num = dices[s][i]
    findMax(s+1, N, t, fs+num)

for i in range(6):                                              # 1번 주사위 윗면을 6개 중에 골라서 함수 시작
    findMax(0, N, dices[0][i], 0)
print(ans)

# 방법 2
import sys
input = sys.stdin.readline
N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
updown = [5, 3, 4, 1, 2, 0]

def findMax(s, N):                                      # s: 현재 주사위, N: 마지막 주사위
    ans = 0                                             # 최댓값
    for i in range(6):                                  # 1번 주사위
        b = dices[s][i]                                 # 아래
        t = dices[s][updown[i]]                         # 위
        result = 0      
        num = 0
        for j in range(6):
            if b == dices[s][j] or t == dices[s][j]:
                continue
            if num < dices[s][j]:
                num = dices[s][j]
        result += num                                   # 옆면 중 최댓값
        
        ns = 1
        while ns <= N-1:                                # 다음 주사위(2~N)
            b = t                                       # 이전 주사위 위가 다음 주사위 아래
            for j in range(6):
                if dices[ns][j] == b:
                    t = dices[ns][updown[j]]
                    break
                    
            num = 0
            for j in range(6):                          
                if b == dices[ns][j] or t == dices[ns][j]:
                    continue
                if num < dices[ns][j]:
                    num = dices[ns][j]
            result += num                               # 옆면 중 최댓값
            ns += 1
            
        if ans < result:                                # 최댓값 저장
            ans = result
    return ans

print(findMax(0, N))