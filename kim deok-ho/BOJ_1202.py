# 작은 가방부터 넣을 수 있는 최대 가치 보석 넣기
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
for _ in range(N):                  # 최소힙, 가벼운 순으로 저장됨
    heappush(jewels, tuple(map(int, input().split())))

bags = [0]*K                           # 최소힙
for i in range(K):
    bags[i] = int(input())
bags.sort()

ans = 0
values = []
for i in range(K):
    bag = bags[i]
    while jewels and bag >= jewels[0][0]:           # 가방에 넣을 수 있는 보석이면 꺼내기
        heappush(values, -heappop(jewels)[1])       # 최대힙으로 저장
    if values:                                      # 비어있지 않으면
        ans += -heappop(values)                     # 꺼내기(최대힙이므로 최댓값이 뽑아짐)
print(ans)