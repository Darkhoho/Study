import sys; input = sys.stdin.readline
def solve():
    cnt = 0
    while True:
        # 배열 순회
        for i in range(n):
            # 중요도가 가장높다면 출력하고 표시
            if li[i] == max(li):
                cnt+=1
                li[i] = 0
                # 만약 출력된 결과물이 뽑아야 되는 서류라면 횟수를 반환
                if i == m:
                    return cnt

for _ in range(int(input())):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    print(solve())