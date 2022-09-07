N, K = map(int, input().split())

temp = list(map(int, input().split()))
ans = 0                             # 처음부터 K번 미리 더해서 구함
for i in range(K):
        ans += temp[i]
now = ans                           # 바꿔갈 값
for i in range(K, N):
    now = now-temp[i-K]+temp[i]     # 가장 앞 값을 빼고 뒤에 값을 추가
    if ans < now:                   # 저장된 값과 비교해서 업데이트
        ans = now
print(ans)

