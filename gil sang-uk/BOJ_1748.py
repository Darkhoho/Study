import sys; input = sys.stdin.readline

n = int(input())
# 글자수 세기
m = len(str(n))
# 가장 마지막 부분 길이 합
result = m*(n-10**(m-1)+1)
# 나머지 부분 각각 더하기
for i in range(m-1):
    result += (9*(10**i))*(i+1)
print(result)