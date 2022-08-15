from sys import stdin

n = int(stdin.readline())
# [시작시작,끝시간]을 담은 이차원 리스트 선언
li = []
for i in range(n):
	li.append(list(map(int,stdin.readline().split())))
# 시작 시간이 어떻게 되든 끝나는 시간이 중요함 (빨리 끝나야 다른 회의를 할 수 있음)
# 끝시간으로 오름차순 정렬 후, 끝시간이 같을 경우 시작시간으로 오름차순 정렬
li.sort(key=lambda x: (x[1],x[0]))
# 제일 처음 값을 뽑아줌 (어차피 제일 처음 값은 들어가야 하기 때문)
confer = [li.pop(0)]
for i in li:
    # 탐색하며 시작 시간이 이미 들어있는 회의의 끝나는 시간보다 같거나 클 경우 추가
    if confer[-1][1] <= i[0]:
        confer.append(i)
print(len(confer))