import sys; input = sys.stdin.readline

n = int(input())
dct = {}
li = [0] * n
total = 0
# 갯수를 담은 딕셔너리
# {key(숫자):value(나온 횟수)}
for i in range(n):
    li[i] = int(input())
    if li[i] in dct:
        dct[li[i]] += 1
    else:
        dct[li[i]] = 1
# 리스트와 딕셔너리 각각 정렬
li.sort()
# 최빈값이 여러개일 때를 대비해 값도 정렬
dct = sorted(dct.items())
dct.sort(key=lambda x:x[1], reverse=True)
# 산술평균
print(round(sum(li)/n))
# 중앙값
print(li[n//2])
# 최빈값
if n > 1:
    # 두개 이상일 때 두번째 값 출력
    if dct[0][1] == dct[1][1]:
        print(dct[1][0])
    else:
        print(dct[0][0])
else:
    print(dct[0][0])
# 범위
print(li[-1] - li[0])