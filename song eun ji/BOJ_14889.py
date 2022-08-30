N = int(input())
team = [list(map(int,input().split())) for i in range(N)]
arr = [i for i in range(N)]
basket = []
all_taste = []

# 부분집합을 만들어서 개수가 N/2인거 먼저 출력하고
for i in range(1 << len(arr)):
    arrnum = []
    for n in range(len(arr)):
        if i & (1 << n):
            arrnum.append(n)
    if len(arrnum) == N//2:
        basket.append(arrnum)

# 차이를 확인하고 가장 작은지 보고
a_taste = b_taste = 0
for i in range(len(basket)//2):
    a_taste = b_taste = 0
    # 스타트 팀 구하고
    for j in basket[i]:
        for k in basket[i]:
            a_taste += team[j][k]

    # 링크 팀 구하고
    for j in basket[-(i+1)]:
        for k in basket[-(i+1)]:
            b_taste += team[j][k]

    all_taste.append(abs(a_taste - b_taste))

print(min(all_taste))