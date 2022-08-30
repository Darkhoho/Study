#회의실개수
T = int(input())

talk = []

# 회의시간을 빠른순으로 정렬
for i in range(T):
    a = list(map(int,input().split()))

    talk.append(a)
    
talk.sort() # 시작시간이 빠른 순으로 정렬
talk.sort(key = lambda x : x[1]) # 끝나는 시간이 빠른 순으로 정렬

count = 1 # 회의실 개수
end_time = talk[0][1] # 정렬한 것의 끝나는 시간
for i in range(1, T):
    if talk[i][0] >= end_time: # 끝나는 시간 뒤의 시작시간이 느리면
        count += 1
        end_time = talk[i][1] #추가하고 끝나는 시간 바꿔주기

print(count)