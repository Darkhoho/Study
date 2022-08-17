for t in range(int(input())):
    N, M = map(int, input().split())
    doc = list(map(int, input().split()))
    i = M
    while i > -1:
        if doc[0] != max(doc):
            doc.append(doc.pop(0))
            if i == 0:
                M += len(doc) - 1
                i += len(doc) - 1
            else:
                M -= 1
                i -= 1
        else:
            doc.pop(0)
            i -= 1
        print(M + 1)
