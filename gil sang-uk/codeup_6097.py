#  배열 선언
arr = []
# 배열 인풋값으로 10*10 채우기
for i in range(10):
    arr.append(list(map(int,input().split())))

# 초기값이 2,2 이므로 인덱스 1,1로 초기화
r,c = 1,1
# 9,9 오른쪽 끝만나면 반복문 종료
while r<9 and c<9:
    # 오른쪽이 1이 아니라면
    if arr[r][c+1] !=1:
        #현재자리 9로
        arr[r][c] = 9
        # 먹이를 만나면 9로 만들고 반복문 종료
        if arr[r][c+1] == 2:
            arr[r][c+1]=9
            break
        #개미 옮기기
        c+=1
        continue
    # 오른쪽이 막혔다면 아래로
    elif arr[r+1][c] !=1:
        arr[r][c] = 9
        if arr[r+1][c] == 2:
            arr[r+1][c]=9
            break
        r+=1
        continue
    # 막혔을 때 현재자리
    arr[r][c]=9
    break

for i in arr:
    print(*i)