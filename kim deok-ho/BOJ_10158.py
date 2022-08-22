# 방법 1 - 원위치 되는 시간을 제거하고 움직임
w, h = map(int, input().split())    # 가로, 세로
p, q = map(int, input().split())    # 개미 위치
t = int(input())                    # 움직이는 시간

pMove = t%(2*w)                     # 원위치 되는 시간 제거
qMove = t%(2*h)                     # 원위치 되는 시간 제거

dp = 1                             # 현재 개미 방향
dq = 1

for i in range(pMove):
    p += dp
    if p < 0 or p > w:              # 양 옆 벽에 닿으면 방향 전환
        p -= dp
        dp = -dp
        p += dp
for i in range(qMove):
    q += dq
    if q < 0 or q > h:              # 위, 아래 벽에 닿으면 방향 전환
        q -= dq
        dq = - dq
        q += dq
print(p, q)                       # 문제의 좌표에 맞춰서 출력

# 방법 2 - 2w와 2h만큼 시간이 지나면 원위치되므로 가로, 세로를 2w와 2h로 계산하고 다시 변환
w, h = map(int, input().split())    # 가로, 세로
p, q = map(int, input().split())    # 개미 위치
t = int(input())                    # 움직이는 시간

# 시간이 2w만큼 원위치되므로 가로를 2w로 두고 넘으면 0부터 시작되는 형태로 변환
# p+t를 2w로 나눈 나머지가 2w에서 현재 위치
# 현재 위치가 w보다 크면 w에서 위치는 w - (p-w)
# 현재 위치가 w보다 작으면 w에서 위치는 그대로
p = (p+t)%(2*w)
if p > w:
    p = 2*w - p

# 세로도 마찬가지
q = (q+t)%(2*h)
if q > h:
    q = 2*h - q

print(p, q)