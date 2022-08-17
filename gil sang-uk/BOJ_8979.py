import sys

n, m = map(int, sys.stdin.readline().split())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
# 금, 은, 동 순으로 정렬
li.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)

for i in range(len(li)):
    # 등수를 알고 싶은 나라
    if li[i][0] == m:
        result = i+1
        # 공동 등수 고려
        while li[i][1:] == li[i-1][1:]:
            result -= 1
            i-=1

print(result)