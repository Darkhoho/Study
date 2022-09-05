# 입력값 받기
N = list(map(int,input()))

# 10까지의 리스트를 일단 만들기
num = [0]*10
# 숫자 집어넣기
for i in N:
    num[i] += 1

# 6과 9는 리스트에 더한 후에 재입력하기
if (num[6] + num[9]) % 2:
    num[6] = (num[6] + num[9]) // 2 + 1
else:
    num[6] = (num[6] + num[9]) // 2

# 가장 많이 필요한 것의 숫자 출력
max_num = num[0]
for i in range(len(num)-1):
    if max_num < num[i]:
        max_num = num[i]
print(f'{max_num}')