# 방법 1
# def dfs(s, N):
#     if num[s-2] == 1 and num[s-1] == 1:
#         return
#     if s == N:
#         global ans
#         ans += 1
#         return
#     num[s] = 1
#     dfs(s+1, N)
#     num[s] = 0
#     dfs(s+1, N)
    
# N = int(input())
# if N <= 2:
#     print(1)
# else:
#     ans = 0
#     num = [1, 0] + [0]*(N-2)
#     dfs(2, N)
#     print(ans)

# 방법 2 - dp
def dp(N):
    ans = [0, 1, 1]
    if N <= 2:
        return ans[N]
    for i in range(3, N+1):
        ans.append(ans[i-1] + ans[i-2])
    return ans[N]

N = int(input())
print(dp(N))
