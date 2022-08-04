#우유가게랑 판매 리스트 받기
num = int(input())
a = list(map(int,input().split()))

#시작은 0에서 시작하므로
s = 0

#먹은 개수
count = 0

#리스트 뽑기
for i in a:
    if i == s:
        #딸기나 초코면 개수 증가 및 스타트 증가
        if s == 0 or s == 1:
            count += 1
            s += 1
        #바나나면 개수증가 및 스타트는 0으로
        elif s ==2:
            s = 0
            count += 1
    #다른경우는 pass
    else:
        pass
print(count)


