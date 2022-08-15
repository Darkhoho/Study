from sys import stdin
# 입력 받기
n = int(stdin.readline())
dist = list(map(int,stdin.readline().split()))
oil = list(map(int,stdin.readline().split()))
# 결과값 초기화, 임시변수는 매우 큰 수로 초기화
result=0
minimum = 999999999999
for i in range(n-1):
    # 이번 도시의 비용과 지금까지 지나친 도시 중 가장 작은 값을 비교
    if oil[i] < minimum:
        minimum = oil[i]
    result += dist[i]*minimum
    
print(result)