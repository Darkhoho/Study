from sys import stdin
# 테스트 케이스
for _ in range(int(stdin.readline())):
    # 한가지 수 받기
    n = int(stdin.readline())
    # 리스트로 받기
    li = list(map(int,stdin.readline().split()))
    # 배열 정렬
    li.sort()
    # 최적의 배열은 작은 순서대로 앞,뒤 번갈아가면서 넣은 배열
    # ex) [1,2,3,4,5] = [1,3,5,4,2]
    # 이 값은 결국 한칸 건넌 수와의 차이를 반영
    # 단, 맨마지막수와 맨 첫 수와의 관계도 반영해야하기 때문에 초기화할 때 넣어줌
    result = li[1]-li[0]
    for i in range(2,n):
        result = max(result,li[i]-li[i-2])
    print(result)