# 방법 1
N = int(input())
M = int(input())

compare = []
for i in range(2*N+1):
    if i%2:
        compare.append('O')
    else:
        compare.append('I')
        
arr = list(input())
point = []
cnt = 0
for i in range(M-(2*N)):
    point.append(i)
    cnt += 1

ans = 0
for i in range(cnt):
    l = point[i]
    r = l + 2*N + 1
    if arr[l:r] == compare:
        ans += 1
print(ans)

# 방법 2
N = int(input())
M = int(input())

compare = ''
for i in range(2*N+1):
    if i%2:
        compare += 'O'
    else:
        compare += 'I'

arr = input()
cnt = 0
i = 0
while i < M-(2*N):
    if arr[i:i+1+(2*N)] == compare:
        cnt += 1
        i += 2
    else:
        i += 1
print(cnt)

# 방법 3
'''
N = IOI의 개수가 됨
1일 때 IOI
2일 때 IOIOI
3일 때 IOIOIOI
IOI의 개수를 카운팅해서 N개가 되면 1개가 만들어진 것!!
'''

N = int(input())
M = int(input())
arr = input()

ans = 0                                 # 목표의 개수
cnt = 0                                 # IOI가 반복된 개수
i = 0
while i < M-2:                          # 3개씩 보기 때문에 M-3 M-2 M-1
    if arr[i:i+3] == 'IOI':
        i += 2                          # 다음 I로 이동
        cnt += 1                        
        if cnt == N:                    # 일치하면 목표 카운팅
            ans += 1
            cnt -= 1                    # 가장 앞에 나온 IOI 빼주기
            
    else:                               # IOI가 만들어지지 않으면 카운트 초기화
        i += 1
        cnt = 0
print(ans)
