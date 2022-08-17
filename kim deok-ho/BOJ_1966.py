# 방법 1
# 테스트 케이스
t = int(input())
for _ in range(t):
    # 문서의 개수, 궁금한 문서의 현재 위치
    n, m = map(int, input().split())
    # n개 문서의 중요도
    importance = list(map(int, input().split()))

    # 순서
    order = 0
    # 목표 위치
    target = m
    idx = 0
    while True:
        # 목표한 문서가 앞에 온 경우
        if idx == target:
            # 중요도가 가장 높으면
            if importance[idx] == max(importance):
                # 순서 1 증가
                order += 1
                # 출력
                print(order)
                break
            # 중요도가 낮으면 뒤로 보내기
            else:
                importance.append(importance.pop(0))
                # 목표 위치 수정
                target = len(importance) - 1
        else:
            # 가장 앞 문서의 중요도가 가장 높으면
            if importance[idx] == max(importance):
                # 순서 1 증가
                order += 1
                # 리스트에서 제거
                importance.pop(0)
                # 목표 위치 수정
                target -= 1
            # 중요도가 낮으면
            else:
                # 가장 뒤로 보내기
                importance.append(importance.pop(0))
                # 목표 위치 수정
                target -= 1

# 방법 2 - deque 사용(FIFO)
from collections import deque
# 테스트 케이스
t = int(input())
for _ in range(t):
    # 문서의 개수, 궁금한 문서의 현재 위치
    n, m = map(int, input().split())
    # n개 문서의 중요도
    importance = deque(map(int, input().split()))

    # 순서
    order = 0
    # 목표 위치
    target = m
    idx = 0
    while True:
        # 목표한 문서가 앞에 온 경우
        if idx == target:
            # 중요도가 가장 높으면
            if importance[idx] == max(importance):
                # 순서 1 증가
                order += 1
                # 출력
                print(order)
                break
            # 중요도가 낮으면 뒤로 보내기
            else:
                importance.append(importance.popleft())
                # 목표 위치 수정
                target = len(importance) - 1
        else:
            # 가장 앞 문서의 중요도가 가장 높으면
            if importance[idx] == max(importance):
                # 순서 1 증가
                order += 1
                # 리스트에서 제거
                importance.popleft()
                # 목표 위치 수정
                target -= 1
            # 중요도가 낮으면
            else:
                # 가장 뒤로 보내기
                importance.append(importance.popleft())
                # 목표 위치 수정
                target -= 1
