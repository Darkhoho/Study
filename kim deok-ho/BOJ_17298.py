# # 방법 1 - 시간 초과
# N = int(input())
# A = list(map(int, input().split()))
#
# for i in range(N-1):
#     for j in range(i+1, N):
#         if A[i] < A[j]:
#             print(A[j], end=' ')
#             break
#     else:
#         print(-1, end=' ')
# print(-1, end=' ')
#
# # 방법 2 - 시간 초과
# N = int(input())
# A = list(map(int, input().split()))
# A.reverse()
# i = N-1
# while i >= 0:
#     i -= 1
#     num = A.pop()
#     if i != -1:
#         for j in range(i, -1, -1):
#             if A[j] > num:
#                 print(A[j], end=' ')
#                 break
#         else:
#             print(-1, end=' ')
#     else:
#         print(-1, end=' ')

# 방법 3 - 시간 초과
# from collections import deque
# N = int(input())
# A = deque(list(map(int, input().split())))
# while N > 0:
#     N -= 1
#     num = A.popleft()
#     if N != 0:
#         for i in range(N):
#             if A[i] > num:
#                 print(A[i], end=' ')
#                 break
#         else:
#             print(-1, end=' ')
#     else:
#         print(-1, end=' ')

# 방법 4
N = int(input())                            # 수열 크기
A = list(map(int, input().split()))         # 수열

stack = []                                  # 스택
ans = [-1]*N                                # 수열의 크기와 같은 리스트를 -1로 초기화

for i in range(N):
    while stack and A[stack[-1]] < A[i]:    # 스택이 비었거나 스택에 쌓인 마지막 값보다 작거나 같으면 종료(오큰수가 아닌 경우까지 반복)
        ans[stack.pop()] = A[i]             # 스택 마지막 값의 오큰수가 됨
    stack.append(i)                         # 오큰수 확인 후 현재 인덱스를 스택에 추가

print(*ans)

# 방법 5
N = int(input())                            # 수열 크기
A = list(map(int, input().split()))         # 수열

stack = [0]                                 # 스택에 첫 인덱스를 미리 대입
ans = [-1]*N                                # 수열의 크기와 같은 리스트를 -1로 초기화

for i in range(1, N):                       # 두 번째 인덱스부터 시작
    while stack and A[stack[-1]] < A[i]:    # 스택이 비었거나 스택에 쌓인 마지막 값보다 작거나 같으면 종료(오큰수가 아닌 경우까지 반복)
        ans[stack.pop()] = A[i]             # 스택 마지막 값의 오큰수가 됨
    stack.append(i)                         # 오큰수 확인 후 현재 인덱스를 스택에 추가

print(*ans)