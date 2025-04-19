n, m, a= map(int, input().split())
counter=0
for i in range(max(n,m)):
    if n==m and n==a:
        counter+=1
        break
    for i in range(n):
        if n==a:
            counter+=1
            break
        n-=a
        counter+=1
        if n<0:
            break
    for i in range(m):
        if m==a:
            counter+=1
            break
        m-=a
        counter+=1
        if m<0:
            break
print(counter)    
    

