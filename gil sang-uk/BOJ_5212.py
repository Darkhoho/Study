import sys;sys.stdin = open('input.txt')
def BFS(y,x):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    cnt = 0
    
    for i in range(4):
        if 0 <= y+dy[i] < len(li) and 0 <= x+dx[i] < len(li[0]):
            if li[y+dy[i]][x+dx[i]] == '.':
                cnt += 1
        else:
            cnt+=1
    if cnt >= 3:
        return (y,x)

def solve():
    for y in range(r):
        for x in range(c):
            if li[y][x] == 'X':
                sink = BFS(y,x)
                if sink:
                    tmp.append(sink)
    for i in tmp:
        y, x = i
        li[y][x] = '.'


r, c = map(int, input().split())
tmp = []
li = []
for _ in range(r):
    li.append(list(input()))
solve()
max_y, min_y, max_x, min_x = 0, 20, 0, 20
for y in range(r):
    for x in range(c):
        if li[y][x] == 'X':
            max_y = max(max_y,y) 
            min_y = min(min_y,y)
            max_x = max(max_x,x)
            min_x = min(min_x,x)
res = []
for y in range(min_y,max_y+1):
    res.append(li[y][min_x:max_x+1])

for i in range(len(res)):
    print(''.join(res[i]))