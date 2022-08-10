m,n = input().split()
m = int(m)
n = int(n)
d=[]
      
for i in range(m) :
    d.append([])
    for j in range(n): 
        d[i].append(0)

t = int(input())
for i in range(t) :
    a = list(map(int,input().split()))
    if a[1] == 0:
        for j in range(a[0]):
            d[a[2]-1][a[3]-1+j] = 1
    elif a[1] == 1:
        for j in range(a[0]):
            d[a[2]-1+j][a[3]-1] = 1

for i in d :
  print(*i)