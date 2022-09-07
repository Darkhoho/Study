from collections import deque

def right(o, r, d):                             # 오른쪽 확인
    for i in range(o + 1, 5):
        if r != arr[i][6]:                      # 왼쪽 톱니의 오른쪽과 현재 톱니의 왼쪽이 다른 경우
            r = arr[i][2]
            if d == -1:
                q[i].append(q[i].popleft())
                d = 1
            else:
                q[i].appendleft(q[i].pop())
                d = -1
        else:
            return
def left(o, l, d):                              # 왼쪽 확인
    for i in range(o - 1, 0, -1):
        if l != arr[i][2]:                      # 오른쪽 톱니의 왼쪽과 현재의 오른쪽이 다른 경우
            l = arr[i][6]
            if d == -1:
                q[i].append(q[i].popleft())
                d = 1
            else:
                q[i].appendleft(q[i].pop())
                d = -1
        else:
            break

arr = [0]*5

for i in range(1, 5):
    arr[i] = deque(list(map(int, input())))
q = deque(arr)

K = int(input())

for _ in range(K):
    o, d = map(int, input().split())
    if o == 1:                                  # 가장 왼쪽 톱니
        r = arr[o][2]
        if d == -1:
            q[o].append(q[o].popleft())
            d = 1
        else:
            q[o].appendleft(q[o].pop())
            d = -1
        right(o, r, d)
    elif o == 4:                                # 가장 오른쪽 톱니
        l = arr[o][6]
        if d == -1:
            q[o].append(q[o].popleft())
            d = 1
        else:
            q[o].appendleft(q[o].pop())
            d = -1
        left(o, l, d)
    else:                                       # 가운데 톱니
        l = arr[o][6]
        r = arr[o][2]
        if d == -1:
            q[o].append(q[o].popleft())
            d = 1
        else:
            q[o].appendleft(q[o].pop())
            d = -1
        right(o, r, d)
        left(o, l, d)

ans = 0
for i in range(1, 5):
    if arr[i][0] == 1:
        ans += 2**(i-1)
print(ans)
