size = int(input())
switch = [0] + list(map(int, input().split()))
personCnt = int(input())
for _ in range(personCnt):
    g, p = map(int, input().split())
    if g == 1:
        for i in range(1, size+1):
            if i%p == 0:
                if switch[i]:
                    switch[i] = 0
                else:
                    switch[i] = 1
    else:
        i = p
        if switch[p]:
            switch[p] = 0
        else:
            switch[p] = 1
        l = p-1
        r = p+1
        while 1 <= l and r <= size:
            if switch[l] == switch[r]:
                if switch[l]:
                    switch[l] = switch[r] = 0
                else:
                    switch[l] = switch[r] = 1
            else:
                break
            l -= 1
            r += 1

for i in range(1, size+1):
    if i % 20:
        print(switch[i], end=' ')
    else:
        print(switch[i])