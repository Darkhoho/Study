# 방법 1 - 완전 탐색
N = int(input())
remoteControl = [1]*10                              # 리모컨 숫자를 인덱스로 번호 상태 확인
M = int(input())                                    # 고장난 개수
if M:
    broken = list(map(int, input().split()))
    for i in range(M):                              # 고장난 번호 체크
        remoteControl[broken[i]] = 0

if N == 100:
    print(0)
else:
    ans = abs(100 - N)
    for num in range(1000001):
        num = str(num)
        length = len(num)
        for i in range(length):
            if remoteControl[int(num[i])] == 0:
                break
        else:
            result = abs(N - int(num)) + length
            if ans > result:
                ans = result
    print(ans)


# 방법 2 - 목표 위치에서 하나씩 줄여서 찾고 하나씩 올려서 찾음
# N = input()
# remoteControl = [1]*10                              # 리모컨 숫자를 인덱스로 번호 상태 확인
# M = int(input())                                    # 고장난 개수
# if M:
#     broken = list(map(int, input().split()))
#     for i in range(M):                              # 고장난 번호 체크
#         remoteControl[broken[i]] = 0

# if N == '100':
#     print(0)
# else:
#     ans = abs(100 - int(N))
#     length = len(N)
#     for i in range(length):
#         if remoteControl[int(N[i])] == 0:
#             now = int(N)
#             while True:
#                 now -= 1
#                 nowLen = len(str(now))
#                 for j in range(nowLen):
#                     if remoteControl[int(str(now)[j])] == 0:
#                         break
#                 else:
#                     ans > nowLen + abs(now - int(N))
#                     ans = nowLen
#                     break
#             now = int(N)
#             while True:
#                 now += 1
#                 nowLen = len(str(now))
#                 for j in range(nowLen):
#                     if remoteControl[int(str(now)[j])] == 0:
#                         break
#                 else:
#                     ans > nowLen + abs(now - int(N))
#                     ans = nowLen
#                     break
#             break
#     else:
#         if ans > len(N):
#             ans = len(N)
#     print(ans)