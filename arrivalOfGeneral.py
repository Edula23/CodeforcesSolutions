size = int(input())
n = list(map(int, input().split()))


counter = 0py
for i in n:
    maxIndex = n.index(max(n))
    if maxIndex==0:
        break
    else:
        n[maxIndex], n[maxIndex-1]=n[maxIndex-1], n[maxIndex]
        counter+=1


for i in n:
    minimum = min(n)
    minIndex = n.index(minimum)
    for i in range(size):
        if n[i]==minimum:
            minIndex=i
    if minIndex==size-1:
        break
    else:
        n[minIndex], n[minIndex+1]=n[minIndex+1], n[minIndex]
        counter+=1

print(counter)