# DFS함수 구현하기
def dfs(v):
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            dfs(w)

# 입력값 받기
computer = int(input())
line = int(input())
G = [[]for i in range(computer+1)]
for i in range(line):
    s, e = map(int,input().split())
    G[s].append(e)
    G[e].append(s)

visited = [0]*(computer+1)

# 1에서부터 출발
dfs(1)

# 몇개에 들렸는지 확인하기
count = 0
for i in range(2,len(visited)):
    if visited[i] == 1:
        count += 1

print(count)