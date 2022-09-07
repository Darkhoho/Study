# 0 0 0이 입력되기 전까지 반복
i = 0 # case 개수 세기 위한, 초기화
while True:
    day = list(map(int,input().split()))
    vac = 0

    if day[0] == 0 and day[1] == 0 and day[2] == 0: # 0, 0, 0이면 break
        break

    else:        
        if day[2]%day[1] <= day[0]: # 연속일수 중 나머지가 휴가 일수보다 작으면
            vac += day[2] % day[1] # 나머지 모두 이용하는 것이므로 나머지 더하기
        else: 
            vac += day[0] # 아니면 휴가일수 만큼 이용하는 것이므로 휴가일수 더하기

        # 나눠서 몫구해서 사용일수랑 곱하고 더하기
        vac += day[2]//day[1] * day[0]
    i += 1
    print(f'Case {i}: {vac}')