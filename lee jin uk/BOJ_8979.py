N, K = map(int, input().split())
medal = [list(map(int, input().split())) for _ in range(N)]
medal.sort()
rank = 1
for n in range(N):
    if medal[K - 1][1] < medal[n][1]:
        rank += 1
    elif medal[K - 1][1] == medal[n][1]:
        if medal[K - 1][2] < medal[n][2]:
            rank += 1
        elif medal[K - 1][2] == medal[n][2]:
            if medal[K - 1][3] < medal[n][3]:
                rank += 1
print(rank)