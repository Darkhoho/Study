N = int(input())
pillar = [list(map(int, input().split())) for _ in range(N)]
pillar.sort()               # 순서대로 나열
ans = 0                     # 넓이

i = 0
while i < N:
    if i != N-1:
        maxH = 0
        idx = 0
        for j in range(i+1, N):
            if maxH <= pillar[j][1]:
                maxH = pillar[j][1]
                idx = j
            if maxH > pillar[i][1]:     # 현재 높이보다 큰 높이가 있으면 그 전까지 넓이 구하기
                ans += pillar[i][1] * (pillar[j][0] - pillar[i][0])
                i = j
                break
        else:                           # 없다면 현재 위치 넓이 더하고 차순위 높이 기둥 전까지 더하기
            ans += pillar[i][1]         
            ans += maxH * (pillar[idx][0] - pillar[i][0] -1)
            i = idx
            continue
    else:                               # 마지막 기둥은 더해지지 않기 때문에 더해주기
        ans += pillar[i][1]
        i += 1
print(ans)
