# 행렬 가로 세로 값 입력받기
r,c = map(int,input().split())
#배열을 모두 0으로 초기화
arr = [[0 for j in range(c)] for i in range(r)]

for i in range(int(input())):
    l,d,y,x = map(int,input().split())
    #길이 만큼 반복
    for j in range(l):
        #가로면 y좌표 고정
        if d == 0:
            arr[y-1][x-1+j] = 1
        #세로면 x좌표 고정
        else:
            arr[y-1+j][x-1] = 1
for i in arr:
    print(*i)