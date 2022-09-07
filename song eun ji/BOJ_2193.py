def hit_2(N):
    if len(zero) <= N+1:
        for i in range(len(zero),N+1):
            one.append(one[i-1] + one[i-2])
            zero.append(zero[i-1] + zero[i-2])

# zero와 one으로 list만들기
zero = [0]*3
one = [0]*3
zero[2] = 1
one[1] = 1

# 입력값 받기
N = int(input())
hit_2(N)
print(zero[N]+one[N])