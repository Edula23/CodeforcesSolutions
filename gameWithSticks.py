n, m = map(int, input().split())
winner = ""
x = max(n, m)
for i in range(x):   
    if n==0 or m==0:
        break
    n-=1
    m-=1
    if i%2==0:
        winner= "Akshat"
    else:
        winner = "Malvika"
print(winner)