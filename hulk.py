n = int(input())
output = ""
for i in range(n):
    if i==n-1 and i%2==0:
        output+="I hate it"
        break
    elif i==n-1 and i%2==1:
        output+="I love it"
        break
    elif i%2==0:
        output+="I hate that "
    elif i%2==1:
        output+="I love that "
print(output)