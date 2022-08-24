N = int(input())

paper = [[0]*100 for _ in range(100)]   # 도화지

for i in range(N):                      # 색종이를 붙임
    x, y = map(int, input().split())
    for r in range(y, y+10):
        for c in range(x, x+10):
            paper[r][c] = 1

ans = 0
for r in range(100):
    for c in range(100):
        if paper[r][c] == 1:            # 색종이가 붙어있으면
            if r == 0 or r == 99:       # 행의 끝이면 둘레 카운트
                ans += 1
            # 위, 아래 색종이가 없으면 카운트
            elif (0 <= r-1 < 100 and paper[r-1][c] == 0) or (0 <= r+1 < 100 and paper[r+1][c] == 0):
                ans += 1
            if c == 0 or c == 99:       # 열의 끝이면 둘레 카운트
                ans += 1
            # 왼쪽, 오른쪽 색종이 없으면 카운트
            elif (0 <= c-1 < 100 and paper[r][c-1] == 0) or (0 <= c+1 < 100 and paper[r][c+1] == 0):
                ans += 1
print(ans)