X, Y = map(int, input().split())
N = int(input())
# 1: 북, 2: 남, 3: 서, 4:동
# 북, 남 - 왼쪽 경계, 동, 서 - 위쪽 경계

def findNS(X, Y, d, x):                 # 경비 위치: 북, 남
    result = 0
    for i in range(N):
        sd, sx = stores[i]
        if sd == d:
            result += abs(x - sx)
        elif sd == 1 or sd == 2:
            result += x+Y+sx if x+Y+sx < X-x+Y+X-sx else X-x+Y+X-sx
        elif sd == 3:
            if d == 1:
                result += x+sx
            else:
                result += x+Y-sx
        else:
            if d == 1:
                result += X-x+sx
            else:
                result += X-x+Y-sx
    return result

def findWE(X, Y, d, x):                 # 경비 위치: 서, 동
    result = 0
    for i in range(N):
        sd, sx = stores[i]
        if sd == d:
            result += abs(x - sx)
        elif sd == 3 or sd == 4:
            result += x+X+sx if x+X+sx < Y-x+X+Y-sx else Y-x+X+Y-sx
        elif sd == 1:
            if d == 3:
                result += x+sx
            else:
                result += x+X-sx
        else:
            if d == 3:
                result += Y-x+sx
            else:
                result += Y-x+X-sx
    return result
stores = [list(map(int, input().split())) for _ in range(N)]

d, x = map(int, input().split())
if d == 1 or d == 2:
    print(findNS(X, Y, d, x))
else:
    print(findWE(X, Y, d, x))
