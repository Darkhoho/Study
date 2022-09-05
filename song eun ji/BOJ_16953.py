# A와 B를 받는다.
a, b = input().split()

n = int(b)
count = 1

# break 되기 전까지 while문 돌리기
while True:
    if n == int(a): # a로 돌아왔다면 계산 횟수 출력 후 break
        print(count)
        break
    elif n < int(a): # 작아진다면 만들 수 없으므로 -1 출력 후 break
        print(-1)
        break
    elif n % 10 == 3 or n % 10 == 5 or n % 10 == 7 or n % 10 == 9:  # 끝자리가 1이외의 홀수라면 계산 불가이므로 -1 출력 후 break
        print(-1)
        break

    elif n % 10: # 값이 홀수라면(1로 끝난다면) 10으로 나눠주기
        n = n // 10
        count += 1

    elif n % 2 == 0: # 짝수이면 2로 나눠주기
        n = n // 2
        count += 1