from collections import deque

def D(d):
    global n
    if d > 0:
        arr.popleft()
    else:
        arr.pop()
    n -= 1

T = int(input())
for _ in range(T):
    d = 1                               # 1 정상방향, -1 뒤집힌 방향
    p = input()
    n = int(input())
    arr = deque(input().lstrip('[').rstrip(']').split(','))
    for ch in p:
        if ch == 'R':
            d *= -1
        else:
            if n == 0:
                arr = 'error'
                break
            D(d)

    if arr == 'error' or arr == []:
        print(arr)
    else:
        arr = list(arr)
        if d > 0:
            ans = '[' + ','.join(arr) + ']'
        else:
            ans = '[' + ','.join(arr[::-1]) + ']'
        print(ans)