import sys;input = sys.stdin.readline
# 1 1
# 2 10
# n n-1 0 : 1 0, 1 : 0
# dp[i] = dp[i-1][0] * 2 + dp[i-1][1]
def solve(n):
    if n <= 2:
        return 1
    ONE = [1, 0] + [0] * (n - 2)
    ZERO = [0, 1] + [0] * (n - 2)
    for i in range(2,n):
        ONE[i] = ZERO[i-1]
        ZERO[i] = ONE[i-1] + ZERO[i-1]
    return ONE[-1] + ZERO[-1]

print(solve(int(input())))