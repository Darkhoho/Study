N = int(input())
A = list(map(int,input().split()))
# index를 담을 stack 선언 후 첫번째 값 할당
idx_lst = [0]
result = [-1]*N
for i in range(1,N):
    # 오큰수를 만났을 때 스택에 담겨있는 인덱스를 꺼내면서 오큰수보다 작은 값을 오큰수로 전부 바꿔줌
    while idx_lst and A[idx_lst[-1]] < A[i]:
        result[idx_lst.pop()] = A[i]
    # 오큰수가 아닐경우 스택에 append
    idx_lst.append(i)

print(*result)