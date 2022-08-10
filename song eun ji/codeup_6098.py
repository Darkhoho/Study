d=[]
for i in range(10) :
  a = list(map(int,input().split()))
  d.append(a)

i=j=1
while i < 10 and j < 10:
    if d[i][j] == 0:
        d[i][j] = 9
        j += 1
    elif d[i][j] == 1:
        j -= 1
        i += 1
    elif d[i][j] == 2:
        d[i][j] = 9
        break

for i in range(10) :
  for j in range(10) : 
    print(d[i][j], end=' ')
  print()