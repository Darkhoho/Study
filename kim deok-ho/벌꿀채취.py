from itertools import permutations
def honeyGet(r, c):                         # 원래 꿀통을 최대 가치로 교체
    if r == N:
        return
    if c + M-1 == N:
        return honeyGet(r+1, 0)

    find = [0]*M                            
    i = 0
    for nc in range(c, c+M):
        find[i] = honeys[r][nc]
        i += 1

    result = 0
    find = list(permutations(find, M))      # 현재 꿀통부터 M개를 포함하는 순열을 만듦
    for i in range(len(find)):              # 꿀을 넣을 수 있는 최댓값을 찾음
        val = 0
        quantity = 0
        for j in range(M):
            quantity += find[i][j]
            val += find[i][j]**2 if quantity <= C else 0
        result = max(result, val)
    honeys[r][c] = result                   # 원래 있던 데이터를 교체
    return honeyGet(r, c+1)

def findMax(r, c):                          # 가능한 범위에서 최댓값을 찾음
    result = 0
    for nr in range(r, N):
        for nc in range(N-M+1):
            if nr == r and nc < c:
                continue
            result = max(result, honeys[nr][nc])
    return result

for case in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    honeys = [list(map(int, input().split())) for _ in range(N)]
    honeyGet(0, 0)
    ans = 0
    for r in range(N):
        for c in range(N-M+1):
            ans = max(ans, honeys[r][c] + findMax(r, c+M))  # 교체된 데이터에서 가능한 최댓값을 찾음
    print(f'#{case} {ans}')
