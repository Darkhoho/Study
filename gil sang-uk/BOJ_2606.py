def DFS(graph,route):
    visited = set()
    stack = [route]

    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.add(tmp)
            stack += graph[tmp]  - visited
                     # {2,6} - {1, 2, 5, 6}
        return len(visited)-1


n = int(input())
# [[][2,4][3][][6][][]]
# {1:{2,5}, 2:{1,3,5}, 3:{2}, 4{7}, 5:{2,6}, 6{5}, 7:{4}}
graph = {}
for _ in range(int(input())):
    s, e = map(int,input().split())
    if s in graph:
        graph[s].add(e)
    else:
        graph[s] = {e}
    if e in graph:
        graph[e].add(s)
    else:
        graph[e] = {s}
    
print(DFS(graph,1))