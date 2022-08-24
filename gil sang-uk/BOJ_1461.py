import sys;input = sys.stdin.readline

# 이분탐색으로 0 찾기
def lowerbound(li, n):
    s, e = 0, len(li)
    while s < e:
        mid = (s + e) // 2
        if n <= li[mid]:
            e = mid
        else:
            s = mid + 1
    return s

n, m = map(int, input().split())
# 0을 넣어서 정렬
li = [0] + list(map(int, input().split()))
li.sort()
# 0의 인덱스 뽑아주기
z = lowerbound(li, 0)
res = 0
# 음수 중에 절댓값이 큰 수부터 m만큼 건너뛰며 왕복
for i in range(0, z, m):
    res += (-li[i]) * 2
# 양수
for i in range(n, z, -m):
    res += li[i] * 2
# 마지막에 가장 큰 경로를 가서 끝내는게 베스트
res -= max(abs(li[0]), abs(li[-1]))
print(res)
