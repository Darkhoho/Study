#test개수
T = int(input())

#통나무 개수와 크기 받기
for i in range(T):
    N = int(input())
    lst_log = list(map(int,input().split()))
    new_lst = []

    lst_log.sort(reverse=True)  #내림차순으로 정렬
    new_lst.append(lst_log[0])  #가장 큰건 일단 넣어두기!

    #가장 큰수를 기준으로 오왼오왼으로 숫자 대입
    if len(lst_log)%2: #홀수일때는 수가 맞으므로 그냥하고
        for i in range(1,len(lst_log),2):
            new_lst.append(lst_log[i])
            new_lst.insert(0,lst_log[i+1])
    else: #짝수 일때는 하나 남으므로 나머지 하나는 나중에 합쳐주기
        for i in range(1,len(lst_log)-1,2):
            new_lst.append(lst_log[i])
            new_lst.insert(0,lst_log[i+1])
        new_lst.append(lst_log[-1])

    # 최소 난이도 크기 출력하기
    m = abs(new_lst[0]-new_lst[1])
    for i in range(1,len(new_lst)-1):
        if m < abs(new_lst[i]-new_lst[i+1]):
            m = abs(new_lst[i]-new_lst[i+1])
            
    # 마지막으로 맨 처음과 끝도 비교해주기   
    if m < abs(new_lst[-1]-new_lst[0]):
        m = abs(new_lst[-1]-new_lst[0])
    print(m)