# N = int(input())
# xy_list = [list(map(int, input().split())) for _ in range(N)]
# xy_list.sort(reverse=True)
# xy_list = sorted(xy_list, key=lambda x: x[1], reverse=True)
# rank = 1
# for n in range(N - 1):
#     if xy_list[n][0] > xy_list[n + 1][0] and xy_list[n][1] > xy_list[n + 1][1]:
#         print(rank, end=' ')
#         rank += 1
#     elif xy_list[n][0] > xy_list[n + 1][0] or xy_list[n][1] > xy_list[n + 1][1]:
#         print(rank, end=' ')



N = int(input())
xy_list = [list(map(int, input().split())) for _ in range(N)]
rank = []
for i in range(N):
    r = 1
    for j in range(N):
        if xy_list[i][0] < xy_list[j][0] and xy_list[i][1] < xy_list[j][1]:
            r += 1
    rank.append(r)
print(*rank)
