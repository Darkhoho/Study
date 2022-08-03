N = int(input())
# 높이를 리스트로 저장
hights = list(map(int,input().split()))

result = 0
tmp = 0
for i in range(N-1):
    # 오르막길 일 경우 높이 차이를 저장
    if hights[i] < hights[i+1]:
        tmp += hights[i+1]-hights[i]
        # 리스트가 끝날 때 가장 높은 높이를 저장
        if i == N-2:
            result = max(tmp,result)
    else:
        # 오르막길이 끝날 때 가장 높은 높이를 저장
        result = max(tmp,result)
        tmp = 0

print(result)