# 방법 1
N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    print(1)
else:
    long = 1
    up = 1
    down = 1
    for i in range(1, N):
        if arr[i] > arr[i-1]:       # 증가하면
            up += 1
            if long < down:         # 감소와 비교
                long = down
            down = 1                # 감소 초기화
            
        elif arr[i] < arr[i-1]:     # 감소하면
            down += 1
            if long < up:           # 증가와 비교
                long = up
            up = 1                  # 증가 초기화
            
        else:                       # 같으면 모두 증가
            down += 1
            up += 1
    if up != 1 or down != 1:        # 비교되지 않고 종료된 것 비교
        long = long if long > (up if up > down else down) else (up if up > down else down)
    print(long)

# 방법 2
N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    print(1)
else:
    stack = [arr[0]]
    for i in range(1, N):

