def totalCheck(x1, y1, p1, q1, x2, y2, p2, q2):
    if dCheck(x1, y1, p1, q1, x2, y2, p2, q2):
        return 'd'
    if cCheck(x1, y1, p1, q1, x2, y2, p2, q2):
        return 'c'
    if bCheck(x1, y1, p1, q1, x2, y2, p2, q2):
        return 'b'
    return 'a'

def dCheck(x1, y1, p1, q1, x2, y2, p2, q2):             # 벗어난 경우
    if x1 > p2 or y1 > q2 or x2 > p1 or y2 >q1:
        return 1

def cCheck(x1, y1, p1, q1, x2, y2, p2, q2):             # 벗어나지 않고 꼭지점이 만나는 경우
    if (x1 == p2 and y1 == q2) or (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2):
        return 1

def bCheck(x1, y1, p1, q1, x2, y2, p2, q2):             # 벗어나지 않고 꼭지점도 안 만나는데 변이 만나는 경우
    if x1 == p2 or p1 == x2 or q1 == y2 or y1 == q2:
        return 1

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    ans = totalCheck(x1, y1, p1, q1, x2, y2, p2, q2)
    print(ans)