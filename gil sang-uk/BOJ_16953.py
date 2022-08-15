from sys import stdin

n, m = map(int,stdin.readline().split())

def ab(n,m):
    cnt = 1
    while m>=n:
        # m과 n이 같다면 반환
        if m == n:
            return cnt
        # 2로 나누어 떨어진다면 2로 나누기
        if m%2 == 0:
            m = m//2
            cnt += 1
        # 맨 뒤가 1이라면 1을 빼기
        elif str(m)[-1] == '1':
            m = m//10
            cnt += 1
        # 두 연산이 불가능 하다면 -1을 반환
        else:
            return -1
    # m이 n보다 작아진다면 불가능 하므로 -1을 반환
    return -1

    
print(ab(n,m))