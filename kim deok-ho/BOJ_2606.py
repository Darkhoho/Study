# 방법 1 - 반복, 스택
N = int(input())    # 컴퓨터 개수
G = int(input())    # 간선 개수

linked = [[] for _ in range(N+1)]       # 간선 리스트
for i in range(G):
    v, w = map(int, input().split())
    linked[v].append(w)
    linked[w].append(v)

visited = [0]*(N+1)                     # 컴퓨터에 바이러스 방문 리스트
v = 1                                   # 시작 1
visited[v] = 1                          # 1번 컴퓨터 바이러스 감염
stack = [v]                             # 스택에 1번 컴퓨터 미리 추가

while stack:                            # 스택이 비었으면 종료
    for w in linked[v]:                 # 현재 컴퓨터와 연결된 컴퓨터 확인
        if visited[w] == 0:             # 바이러스가 방문하지 않은 경우
            stack.append(v)             # 스택에 현재 컴퓨터 추가
            v = w                       # w 컴퓨터에 방문
            visited[v] = 1
            break
    else:                               # 연결된 컴퓨터 중 감염되지 않은 컴퓨터가 없으면
        v = stack.pop()                 # 이전 컴퓨터로 돌아감

print(sum(visited)-1)                   # 1번 컴퓨터를 빼고 출력

# 방법 2 - 재귀 함수
N = int(input())    # 컴퓨터 개수
G = int(input())    # 간선 개수

linked = [[] for _ in range(N+1)]       # 간선 리스트

for i in range(G):
    v, w = map(int, input().split())
    linked[v].append(w)
    linked[w].append(v)

visited = [0]*(N+1)                     # 컴퓨터에 바이러스 감염 리스트
v = 1                                   # 시작 1
cnt = 0
def dfs(v):
    global cnt
    visited[v] = 1                      # 현재 컴퓨터 바이러스 감염
    for w in linked[v]:                 # 연결된 컴퓨터 중 감염되지 않은 컴퓨터 찾기
        if visited[w] != 1:
            cnt += 1
            dfs(w)
dfs(v)
print(cnt)