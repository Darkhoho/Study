test_num = int(input())
up = list(map(int,input().split()))

up_1 = up_2 = up[0]
ups = []
for i in range(1,len(up)):
    if up_2 < up[i]:
        up_count = up[i]-up_1
        up_2 = up[i]
        ups.append(up_count)


    elif up_2 == up[i]:
        up_1 = up_2 = up[i]
    
    elif up_2 > up[i]:
        up_1 = up_2 = up[i]
    
if ups != []:
    print(max(ups))
else:
    print(0)


